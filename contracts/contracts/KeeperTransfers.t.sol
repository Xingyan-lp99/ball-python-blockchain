// SPDX-License-Identifier: UNLICENSED
pragma solidity 0.8.28;

import {SnakeRegistry} from "./SnakeRegistry.sol";
import {KeeperTransfers} from "./KeeperTransfers.sol";

interface VmKeeperTransfersTest {
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

contract KeeperTransfersTest {
    VmKeeperTransfersTest private constant VM =
        VmKeeperTransfersTest(
            address(uint160(uint256(keccak256("hevm cheat code"))))
        );

    address private constant SELLER = address(0xB001);
    address private constant BUYER = address(0xB002);
    address private constant OUTSIDER = address(0xB003);

    string private constant SNAKE_ID = "SNAKE001";

    SnakeRegistry private registry;
    KeeperTransfers private transfers;

    event KeeperTransferAccepted(
        string indexed snakeId,
        address indexed fromKeeper,
        address indexed recipient
    );

    // Prepare an independent registered snake before each test.
    // Without this setup, tests would lack the initial keeper and registry link.
    function setUp() public {
        registry = new SnakeRegistry();
        transfers = new KeeperTransfers(address(registry));

        VM.prank(SELLER);
        registry.registerSnake(SNAKE_ID);
    }

    // Check that an unrelated account cannot initiate a handover.
    // Removing this test loses coverage of the current-keeper restriction.
    function testOutsiderCannotInitiateTransfer() public {
        VM.expectRevert(KeeperTransfers.NotCurrentKeeper.selector);
        VM.prank(OUTSIDER);
        transfers.initiateKeeperTransfer(SNAKE_ID, BUYER);

        require(
            transfers.getCurrentKeeper(SNAKE_ID) == SELLER,
            "Rejected initiation must preserve keeper"
        );

        (address fromKeeper, address recipient, bool pending) =
            transfers.getPendingKeeperTransfer(SNAKE_ID);

        require(!pending, "Rejected initiation must not create a proposal");
        require(fromKeeper == address(0), "No sender should be stored");
        require(recipient == address(0), "No recipient should be stored");
    }

    // Check that initiation records the proposal without transferring authority.
    // Removing this test loses coverage of the buyer-consent waiting stage.
    function testInitiationKeepsSellerUntilAcceptance() public {
        require(
            transfers.getCurrentKeeper(SNAKE_ID) == SELLER,
            "Initial keeper must come from SnakeRegistry"
        );

        VM.prank(SELLER);
        transfers.initiateKeeperTransfer(SNAKE_ID, BUYER);

        require(
            transfers.getCurrentKeeper(SNAKE_ID) == SELLER,
            "Initiation must not change keeper"
        );

        (address fromKeeper, address recipient, bool pending) =
            transfers.getPendingKeeperTransfer(SNAKE_ID);

        require(pending, "A proposal must await acceptance");
        require(fromKeeper == SELLER, "Proposal sender must be seller");
        require(recipient == BUYER, "Proposal recipient must be buyer");
    }

    // Check that an unrelated account cannot accept the buyer's proposal.
    // Removing this test loses coverage of designated-recipient authorization.
    function testOutsiderCannotAcceptTransfer() public {
        VM.prank(SELLER);
        transfers.initiateKeeperTransfer(SNAKE_ID, BUYER);

        VM.expectRevert(KeeperTransfers.NotDesignatedRecipient.selector);
        VM.prank(OUTSIDER);
        transfers.acceptKeeperTransfer(SNAKE_ID);

        require(
            transfers.getCurrentKeeper(SNAKE_ID) == SELLER,
            "Rejected acceptance must preserve keeper"
        );

        (address fromKeeper, address recipient, bool pending) =
            transfers.getPendingKeeperTransfer(SNAKE_ID);

        require(pending, "Rejected acceptance must preserve proposal");
        require(fromKeeper == SELLER, "Proposal sender must remain seller");
        require(recipient == BUYER, "Proposal recipient must remain buyer");
    }

    // Check the completed handover, its event, and cleared pending state.
    // Removing this test loses coverage of the successful authority change.
    function testBuyerAcceptanceUpdatesKeeperAndEmitsEvent() public {
        VM.prank(SELLER);
        transfers.initiateKeeperTransfer(SNAKE_ID, BUYER);

        VM.expectEmit(true, true, true, true, address(transfers));
        emit KeeperTransferAccepted(SNAKE_ID, SELLER, BUYER);

        VM.prank(BUYER);
        transfers.acceptKeeperTransfer(SNAKE_ID);

        require(
            transfers.getCurrentKeeper(SNAKE_ID) == BUYER,
            "Accepted buyer must become current keeper"
        );

        (address fromKeeper, address recipient, bool pending) =
            transfers.getPendingKeeperTransfer(SNAKE_ID);

        require(!pending, "Acceptance must clear the pending proposal");
        require(fromKeeper == address(0), "Pending sender must be cleared");
        require(recipient == address(0), "Pending recipient must be cleared");

        require(
            registry.getCurrentKeeper(SNAKE_ID) == SELLER,
            "Original registry must retain the initial keeper"
        );
    }
        event KeeperTransferRejected(
        string indexed snakeId,
        address indexed fromKeeper,
        address indexed recipient
    );

    event KeeperTransferCancelled(
        string indexed snakeId,
        address indexed fromKeeper,
        address indexed recipient
    );

    // Check the complete pending state after a transfer operation.
    // Without these assertions, a test could miss altered parties or stale data.
    function _assertPendingState(
        address expectedSender,
        address expectedRecipient,
        bool expectedPending
    ) private view {
        (address fromKeeper, address recipient, bool pending) =
            transfers.getPendingKeeperTransfer(SNAKE_ID);

        require(pending == expectedPending, "Unexpected pending flag");
        require(fromKeeper == expectedSender, "Unexpected pending sender");
        require(recipient == expectedRecipient, "Unexpected pending recipient");
    }

    // Check buyer rejection, its event, and the ability to propose again.
    // Removing this test loses coverage of a declined handover's lifecycle.
    function testBuyerRejectionPreservesKeeperAndAllowsNewProposal() public {
        VM.prank(SELLER);
        transfers.initiateKeeperTransfer(SNAKE_ID, BUYER);

        VM.expectEmit(true, true, true, true, address(transfers));
        emit KeeperTransferRejected(SNAKE_ID, SELLER, BUYER);

        VM.prank(BUYER);
        transfers.rejectKeeperTransfer(SNAKE_ID);

        require(
            transfers.getCurrentKeeper(SNAKE_ID) == SELLER,
            "Rejection must preserve seller authority"
        );
        _assertPendingState(address(0), address(0), false);

        VM.prank(SELLER);
        transfers.initiateKeeperTransfer(SNAKE_ID, BUYER);

        _assertPendingState(SELLER, BUYER, true);
    }

    // Check seller cancellation, its event, and the ability to propose again.
    // Removing this test loses coverage of withdrawal before buyer acceptance.
    function testSellerCancellationPreservesKeeperAndAllowsNewProposal() public {
        VM.prank(SELLER);
        transfers.initiateKeeperTransfer(SNAKE_ID, BUYER);

        VM.expectEmit(true, true, true, true, address(transfers));
        emit KeeperTransferCancelled(SNAKE_ID, SELLER, BUYER);

        VM.prank(SELLER);
        transfers.cancelKeeperTransfer(SNAKE_ID);

        require(
            transfers.getCurrentKeeper(SNAKE_ID) == SELLER,
            "Cancellation must preserve seller authority"
        );
        _assertPendingState(address(0), address(0), false);

        VM.prank(SELLER);
        transfers.initiateKeeperTransfer(SNAKE_ID, BUYER);

        _assertPendingState(SELLER, BUYER, true);
    }

    // Check that another account cannot decline the buyer's proposal.
    // Removing this test loses coverage of rejection permission enforcement.
    function testOutsiderCannotRejectTransfer() public {
        VM.prank(SELLER);
        transfers.initiateKeeperTransfer(SNAKE_ID, BUYER);

        VM.expectRevert(KeeperTransfers.NotDesignatedRecipient.selector);
        VM.prank(OUTSIDER);
        transfers.rejectKeeperTransfer(SNAKE_ID);

        require(
            transfers.getCurrentKeeper(SNAKE_ID) == SELLER,
            "Unauthorized rejection must preserve keeper"
        );
        _assertPendingState(SELLER, BUYER, true);
    }

    // Check that another account cannot withdraw the seller's proposal.
    // Removing this test loses coverage of cancellation permission enforcement.
    function testOutsiderCannotCancelTransfer() public {
        VM.prank(SELLER);
        transfers.initiateKeeperTransfer(SNAKE_ID, BUYER);

        VM.expectRevert(KeeperTransfers.NotCurrentKeeper.selector);
        VM.prank(OUTSIDER);
        transfers.cancelKeeperTransfer(SNAKE_ID);

        require(
            transfers.getCurrentKeeper(SNAKE_ID) == SELLER,
            "Unauthorized cancellation must preserve keeper"
        );
        _assertPendingState(SELLER, BUYER, true);
    }

    // Check that a second proposal cannot replace the pending recipient.
    // Removing this test loses coverage of the one-pending-proposal rule.
    function testDuplicateInitiationPreservesOriginalProposal() public {
        VM.prank(SELLER);
        transfers.initiateKeeperTransfer(SNAKE_ID, BUYER);

        VM.expectRevert(KeeperTransfers.TransferAlreadyPending.selector);
        VM.prank(SELLER);
        transfers.initiateKeeperTransfer(SNAKE_ID, OUTSIDER);

        require(
            transfers.getCurrentKeeper(SNAKE_ID) == SELLER,
            "Duplicate initiation must preserve keeper"
        );
        _assertPendingState(SELLER, BUYER, true);
    }

    // Check that a completed proposal cannot be accepted again.
    // Removing this test loses coverage of repeated acceptance after resolution.
    function testRepeatedAcceptanceIsRejected() public {
        VM.prank(SELLER);
        transfers.initiateKeeperTransfer(SNAKE_ID, BUYER);

        VM.prank(BUYER);
        transfers.acceptKeeperTransfer(SNAKE_ID);

        VM.expectRevert(KeeperTransfers.NoPendingTransfer.selector);
        VM.prank(BUYER);
        transfers.acceptKeeperTransfer(SNAKE_ID);

        require(
            transfers.getCurrentKeeper(SNAKE_ID) == BUYER,
            "Repeated acceptance must preserve buyer authority"
        );
        _assertPendingState(address(0), address(0), false);
    }
}