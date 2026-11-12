// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.34;

import {Test} from "forge-std/Test.sol";
import {SnakeRegistry} from "./SnakeRegistry.sol";

contract SnakeRegistryTest is Test {
  SnakeRegistry registry;
  event SnakeRegistered(string snakeId, address indexed manager);

  function setUp() public {
    registry = new SnakeRegistry(bytes32(uint256(17)));
  }

  function test_RegisterBindsCallerAndEmitsEvidence() public {
    address breeder = address(0xB001);
    vm.expectEmit(false, true, false, true);
    emit SnakeRegistered("S001", breeder);
    vm.prank(breeder);
    registry.register("S001");
    assertEq(registry.managerOf("S001"), breeder);
  }

  function test_RejectDuplicateFromAnotherCaller() public {
    registry.register("S001");
    vm.prank(address(0xB002));
    vm.expectRevert(SnakeRegistry.SnakeAlreadyRegistered.selector);
    registry.register("S001");
    assertEq(registry.managerOf("S001"), address(this));
  }

  function test_RejectEmpty() public {
    vm.expectRevert(SnakeRegistry.EmptySnakeId.selector);
    registry.register("");
  }

  function test_RejectWhitespaceOnly() public {
    vm.expectRevert(SnakeRegistry.EmptySnakeId.selector);
    registry.register(" \t\n");
  }

  function test_UnknownAndDeploymentInstance() public view {
    assertEq(registry.managerOf("missing"), address(0));
    assertEq(registry.instanceId(), bytes32(uint256(17)));
  }
}
