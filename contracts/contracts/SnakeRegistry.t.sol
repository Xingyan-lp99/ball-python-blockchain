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
    address private constant BUYER_B = address(0xB003);

    SnakeRegistry private registry;

    event SnakeRegistered(string snakeId, address keeper);
    event KeeperTransferInitiated(
        string indexed snakeId,
        address indexed fromKeeper,
        address indexed recipient
    );

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

    function testKeeperCanTransferFromBreederToBuyerAToBuyerB() public {
        VM.prank(BREEDER);
        registry.registerSnake("SNAKE001");

        VM.prank(BREEDER);
        registry.initiateKeeperTransfer("SNAKE001", BUYER);

        VM.prank(BUYER);
        registry.acceptKeeperTransfer("SNAKE001");

        require(
            registry.getCurrentKeeper("SNAKE001") == BUYER,
            "Buyer A must become keeper after acceptance"
        );

        VM.prank(BUYER);
        registry.initiateKeeperTransfer("SNAKE001", BUYER_B);

        VM.prank(BUYER_B);
        registry.acceptKeeperTransfer("SNAKE001");

        require(
            registry.getCurrentKeeper("SNAKE001") == BUYER_B,
            "Buyer B must become keeper after acceptance"
        );

        (address fromKeeper, address recipient, bool pending) = registry
            .getPendingKeeperTransfer("SNAKE001");

        require(!pending, "Accepted transfer must be cleared");
        require(fromKeeper == address(0), "No pending sender must remain");
        require(recipient == address(0), "No pending recipient must remain");
    }

    function testOnlyCurrentKeeperCanInitiateTransfer() public {
        VM.prank(BREEDER);
        registry.registerSnake("SNAKE001");

        VM.expectRevert(SnakeRegistry.NotCurrentKeeper.selector);
        VM.prank(BUYER);
        registry.initiateKeeperTransfer("SNAKE001", BUYER_B);
    }

    function testOnlyDesignatedRecipientCanAcceptTransfer() public {
        VM.prank(BREEDER);
        registry.registerSnake("SNAKE001");

        VM.prank(BREEDER);
        registry.initiateKeeperTransfer("SNAKE001", BUYER);

        VM.expectRevert(SnakeRegistry.NotDesignatedRecipient.selector);
        VM.prank(BREEDER);
        registry.acceptKeeperTransfer("SNAKE001");

        require(
            registry.getCurrentKeeper("SNAKE001") == BREEDER,
            "Keeper must not change before recipient acceptance"
        );
    }

    function testRecipientCanRejectWithoutChangingKeeper() public {
        VM.prank(BREEDER);
        registry.registerSnake("SNAKE001");

        VM.prank(BREEDER);
        registry.initiateKeeperTransfer("SNAKE001", BUYER);

        VM.prank(BUYER);
        registry.rejectKeeperTransfer("SNAKE001");

        require(
            registry.getCurrentKeeper("SNAKE001") == BREEDER,
            "Rejecting transfer must preserve keeper"
        );

        (, , bool pending) = registry.getPendingKeeperTransfer("SNAKE001");
        require(!pending, "Rejected transfer must be cleared");
    }

    function testCurrentKeeperCanCancelTransfer() public {
        VM.prank(BREEDER);
        registry.registerSnake("SNAKE001");

        VM.prank(BREEDER);
        registry.initiateKeeperTransfer("SNAKE001", BUYER);

        VM.prank(BREEDER);
        registry.cancelKeeperTransfer("SNAKE001");

        require(
            registry.getCurrentKeeper("SNAKE001") == BREEDER,
            "Canceling transfer must preserve keeper"
        );

        (, , bool pending) = registry.getPendingKeeperTransfer("SNAKE001");
        require(!pending, "Canceled transfer must be cleared");
    }

    function testRecipientCannotCancelTransfer() public {
        VM.prank(BREEDER);
        registry.registerSnake("SNAKE001");

        VM.prank(BREEDER);
        registry.initiateKeeperTransfer("SNAKE001", BUYER);

        VM.expectRevert(SnakeRegistry.NotCurrentKeeper.selector);
        VM.prank(BUYER);
        registry.cancelKeeperTransfer("SNAKE001");
    }

    function testOnlyOneTransferCanBePendingPerSnake() public {
        VM.prank(BREEDER);
        registry.registerSnake("SNAKE001");

        VM.prank(BREEDER);
        registry.initiateKeeperTransfer("SNAKE001", BUYER);

        VM.expectRevert(SnakeRegistry.TransferAlreadyPending.selector);
        VM.prank(BREEDER);
        registry.initiateKeeperTransfer("SNAKE001", BUYER_B);
    }

    function testZeroAddressCannotBeTransferRecipient() public {
        VM.prank(BREEDER);
        registry.registerSnake("SNAKE001");

        VM.expectRevert(SnakeRegistry.ZeroAddress.selector);
        VM.prank(BREEDER);
        registry.initiateKeeperTransfer("SNAKE001", address(0));
    }

    function testCurrentKeeperCannotTransferToItself() public {
        VM.prank(BREEDER);
        registry.registerSnake("SNAKE001");

        VM.expectRevert(SnakeRegistry.SameKeeper.selector);
        VM.prank(BREEDER);
        registry.initiateKeeperTransfer("SNAKE001", BREEDER);
    }

    function testUnknownSnakeCannotStartTransfer() public {
        VM.expectRevert(SnakeRegistry.SnakeNotFound.selector);
        VM.prank(BREEDER);
        registry.initiateKeeperTransfer("SNAKE999", BUYER);
    }

    function testTransferInitiationEmitsEvent() public {
        VM.prank(BREEDER);
        registry.registerSnake("SNAKE001");

        VM.expectEmit(true, true, true, false, address(registry));
        emit KeeperTransferInitiated("SNAKE001", BREEDER, BUYER);

        VM.prank(BREEDER);
        registry.initiateKeeperTransfer("SNAKE001", BUYER);
    }
}
