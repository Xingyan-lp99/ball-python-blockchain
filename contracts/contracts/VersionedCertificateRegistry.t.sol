// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.34;
import {Test} from "forge-std/Test.sol";
import {SnakeRegistry} from "./SnakeRegistry.sol";
import {VersionedCertificateRegistry} from "./VersionedCertificateRegistry.sol";

contract VersionedCertificateRegistryTest is Test {
  VersionedCertificateRegistry registry;
  address lab = address(0x1AB001);
  address otherLab = address(0x1AB002);
  bytes32 firstHash = sha256("TEST ONLY V1");
  bytes32 secondHash = sha256("TEST ONLY V2");
  event CertificateIssued(string certificateId, string snakeId, address indexed issuer, uint256 version, bytes32 fileHash);

  function setUp() public {
    SnakeRegistry snakes = new SnakeRegistry(bytes32(uint256(1)));
    snakes.register("TEST-S001");
    registry = new VersionedCertificateRegistry(bytes32(uint256(2)), address(snakes));
    registry.authorizeLaboratory(lab);
    registry.authorizeLaboratory(otherLab);
    vm.prank(lab);
    registry.issueVersion("CERT-LAB001-BP-S001", "TEST-S001", 1, firstHash);
  }

  function test_OriginalAuthorizedIssuerAppendsAndEmits() public {
    vm.expectEmit(false, true, false, true);
    emit CertificateIssued("CERT-LAB001-BP-S001", "TEST-S001", lab, 2, secondHash);
    vm.prank(lab);
    registry.issueVersion("CERT-LAB001-BP-S001", "TEST-S001", 2, secondHash);
    assertEq(registry.latestVersion("CERT-LAB001-BP-S001"), 2);
    assertEq(registry.getVersion("CERT-LAB001-BP-S001", 1).fileHash, firstHash);
    assertEq(registry.getVersion("CERT-LAB001-BP-S001", 2).fileHash, secondHash);
  }

  function test_OtherAuthorizedLabCannotAppend() public {
    vm.prank(otherLab);
    vm.expectRevert(VersionedCertificateRegistry.NotOriginalIssuer.selector);
    registry.issueVersion("CERT-LAB001-BP-S001", "TEST-S001", 2, secondHash);
  }

  function test_BreederAndBuyerCannotAppend() public {
    vm.expectRevert(VersionedCertificateRegistry.Unauthorized.selector);
    registry.issueVersion("CERT-LAB001-BP-S001", "TEST-S001", 2, secondHash);
    vm.prank(address(0xB0B));
    vm.expectRevert(VersionedCertificateRegistry.Unauthorized.selector);
    registry.issueVersion("CERT-LAB001-BP-S001", "TEST-S001", 2, secondHash);
  }

  function test_DeauthorizedOriginalLabCannotAppend() public {
    registry.setLaboratoryAuthorization(lab, false);
    vm.prank(lab);
    vm.expectRevert(VersionedCertificateRegistry.Unauthorized.selector);
    registry.issueVersion("CERT-LAB001-BP-S001", "TEST-S001", 2, secondHash);
    assertEq(registry.latestVersion("CERT-LAB001-BP-S001"), 1);
  }

  function test_CannotSkipOrOverwriteVersions() public {
    vm.startPrank(lab);
    vm.expectRevert(VersionedCertificateRegistry.InvalidVersion.selector);
    registry.issueVersion("CERT-LAB001-BP-S001", "TEST-S001", 3, secondHash);
    vm.expectRevert(VersionedCertificateRegistry.InvalidVersion.selector);
    registry.issueVersion("CERT-LAB001-BP-S001", "TEST-S001", 1, secondHash);
    registry.issueVersion("CERT-LAB001-BP-S001", "TEST-S001", 2, secondHash);
    vm.expectRevert(VersionedCertificateRegistry.InvalidVersion.selector);
    registry.issueVersion("CERT-LAB001-BP-S001", "TEST-S001", 2, secondHash);
    vm.stopPrank();
    assertEq(registry.getVersion("CERT-LAB001-BP-S001", 1).fileHash, firstHash);
  }

  function test_SnakeCannotChangeAndFailureKeepsLatest() public {
    vm.prank(lab);
    vm.expectRevert(VersionedCertificateRegistry.SeriesImmutable.selector);
    registry.issueVersion("CERT-LAB001-BP-S001", "OTHER-SNAKE", 2, secondHash);
    assertEq(registry.latestVersion("CERT-LAB001-BP-S001"), 1);
  }

  function test_AdminAuthorizationIsRestricted() public {
    vm.prank(lab);
    vm.expectRevert(VersionedCertificateRegistry.Unauthorized.selector);
    registry.setLaboratoryAuthorization(lab, true);
  }
}
