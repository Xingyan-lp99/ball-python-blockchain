// SPDX-License-Identifier: UNLICENSED
pragma solidity 0.8.28;

import {SnakeRegistry} from "./SnakeRegistry.sol";

interface Vm {
    function prank(address sender) external;

    function expectRevert(bytes4 selector) external;

    function expectEmit(
        bool checkTopic1,
        bool checkTopic2,
        bool checkTopic3,
        bool checkData,
        address emitter
    ) external;
}

contract SnakeRegistryTest {
    Vm private constant VM =
        Vm(address(uint160(uint256(keccak256("hevm cheat code")))));

    address private constant BREEDER = address(0xB001);
    address private constant BUYER = address(0xB002);

    SnakeRegistry private registry;

    event SnakeRegistered(string snakeId, address keeper);

    function setUp() public {
        registry = new SnakeRegistry();
    }

    function testRegistrationSetsSenderAsKeeper() public {
        VM.prank(BREEDER);
        registry.registerSnake("SNAKE001");

        require(
            registry.getCurrentKeeper("SNAKE001") == BREEDER,
            "Initial keeper must be the registering sender"
        );
    }

    function testRegistrationEmitsEvent() public {
        VM.expectEmit(false, false, false, true, address(registry));
        emit SnakeRegistered("SNAKE001", BREEDER);

        VM.prank(BREEDER);
        registry.registerSnake("SNAKE001");
    }

    function testEmptyIdentifierIsRejected() public {
        VM.expectRevert(SnakeRegistry.EmptySnakeId.selector);

        VM.prank(BREEDER);
        registry.registerSnake("");
    }

    function testSameCallerCannotRegisterDuplicate() public {
        VM.prank(BREEDER);
        registry.registerSnake("SNAKE001");

        VM.expectRevert(SnakeRegistry.SnakeAlreadyRegistered.selector);

        VM.prank(BREEDER);
        registry.registerSnake("SNAKE001");

        require(
            registry.getCurrentKeeper("SNAKE001") == BREEDER,
            "Duplicate registration must preserve keeper"
        );
    }

    function testDifferentCallerCannotOverwriteKeeper() public {
        VM.prank(BREEDER);
        registry.registerSnake("SNAKE001");

        VM.expectRevert(SnakeRegistry.SnakeAlreadyRegistered.selector);

        VM.prank(BUYER);
        registry.registerSnake("SNAKE001");

        require(
            registry.getCurrentKeeper("SNAKE001") == BREEDER,
            "Another caller must not overwrite keeper"
        );
    }

    function testUnknownIdentifierIsRejected() public {
        VM.expectRevert(SnakeRegistry.SnakeNotFound.selector);
        registry.getCurrentKeeper("SNAKE999");
    }

    function testRegistrationDoesNotRequireWhitelist() public {
        VM.prank(BUYER);
        registry.registerSnake("SNAKE002");

        require(
            registry.getCurrentKeeper("SNAKE002") == BUYER,
            "Any caller may register an unused identifier"
        );
    }

    function testIdentifiersUseExactStrings() public {
        VM.prank(BREEDER);
        registry.registerSnake("SNAKE001");

        VM.prank(BUYER);
        registry.registerSnake("snake001");

        VM.prank(BUYER);
        registry.registerSnake("SNAKE001 ");

        VM.prank(BUYER);
        registry.registerSnake(" ");

        require(
            registry.getCurrentKeeper("SNAKE001") == BREEDER,
            "Original identifier must retain its keeper"
        );
        require(
            registry.getCurrentKeeper("snake001") == BUYER,
            "Case must remain distinct"
        );
        require(
            registry.getCurrentKeeper("SNAKE001 ") == BUYER,
            "Trailing spaces must remain distinct"
        );
        require(
            registry.getCurrentKeeper(" ") == BUYER,
            "Whitespace-only identifier is nonempty"
        );
    }
}