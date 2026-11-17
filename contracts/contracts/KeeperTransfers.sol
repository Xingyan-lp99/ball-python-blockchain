// SPDX-License-Identifier: UNLICENSED
pragma solidity 0.8.28;

interface IInitialKeeperRegistry {
    function getCurrentKeeper(
        string calldata snakeId
    ) external view returns (address);
}

/// @notice Keeper transfers for snakes registered in the existing SnakeRegistry.
/// @dev Adapted from keeper-transfer commit b527c1c without replacing that registry.
contract KeeperTransfers {
    struct PendingKeeperTransfer {
        address fromKeeper;
        address recipient;
        bool exists;
    }

    IInitialKeeperRegistry public immutable snakeRegistry;

    mapping(string => address) private transferredKeepers;
    mapping(string => PendingKeeperTransfer) private pendingKeeperTransfers;

    error ZeroAddress();
    error InvalidSnakeRegistry();
    error SnakeNotFound();
    error SameKeeper();
    error TransferAlreadyPending();
    error NoPendingTransfer();
    error NotCurrentKeeper();
    error NotDesignatedRecipient();
    error InvalidTransferState();

    event KeeperTransferInitiated(
        string indexed snakeId,
        address indexed fromKeeper,
        address indexed recipient
    );
    event KeeperTransferAccepted(
        string indexed snakeId,
        address indexed fromKeeper,
        address indexed recipient
    );
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

    constructor(address snakeRegistryAddress) {
        if (snakeRegistryAddress == address(0)) {
            revert ZeroAddress();
        }
        if (snakeRegistryAddress.code.length == 0) {
            revert InvalidSnakeRegistry();
        }
        snakeRegistry = IInitialKeeperRegistry(snakeRegistryAddress);
    }

    // Read the accepted keeper, falling back to the original registration keeper.
    // Removing this fallback would require registering existing snakes again.
    function getCurrentKeeper(
        string calldata snakeId
    ) public view returns (address) {
        address keeper = transferredKeepers[snakeId];
        if (keeper == address(0)) {
            keeper = snakeRegistry.getCurrentKeeper(snakeId);
        }
        if (keeper == address(0)) {
            revert SnakeNotFound();
        }
        return keeper;
    }

    // Initiation reserves one recipient but leaves the current keeper unchanged.
    // Without this step, the buyer would have no pending transfer to accept.
    function initiateKeeperTransfer(
        string calldata snakeId,
        address recipient
    ) external {
        address currentKeeper = getCurrentKeeper(snakeId);
        if (msg.sender != currentKeeper) {
            revert NotCurrentKeeper();
        }
        if (recipient == address(0)) {
            revert ZeroAddress();
        }
        if (recipient == currentKeeper) {
            revert SameKeeper();
        }
        if (pendingKeeperTransfers[snakeId].exists) {
            revert TransferAlreadyPending();
        }

        pendingKeeperTransfers[snakeId] = PendingKeeperTransfer({
            fromKeeper: currentKeeper,
            recipient: recipient,
            exists: true
        });
        emit KeeperTransferInitiated(snakeId, currentKeeper, recipient);
    }

    // Only acceptance by the designated recipient changes keeper authority.
    // Without this operation, pending transfers could never complete.
    function acceptKeeperTransfer(string calldata snakeId) external {
        PendingKeeperTransfer storage transfer = pendingKeeperTransfers[snakeId];
        if (!transfer.exists) {
            revert NoPendingTransfer();
        }
        if (msg.sender != transfer.recipient) {
            revert NotDesignatedRecipient();
        }
        if (getCurrentKeeper(snakeId) != transfer.fromKeeper) {
            revert InvalidTransferState();
        }

        address previousKeeper = transfer.fromKeeper;
        address newKeeper = transfer.recipient;
        transferredKeepers[snakeId] = newKeeper;
        delete pendingKeeperTransfers[snakeId];
        emit KeeperTransferAccepted(snakeId, previousKeeper, newKeeper);
    }

    // Rejection clears the proposal without changing keeper or deleting history.
    // Without it, the recipient could not explicitly decline the transfer.
    function rejectKeeperTransfer(string calldata snakeId) external {
        PendingKeeperTransfer storage transfer = pendingKeeperTransfers[snakeId];
        if (!transfer.exists) {
            revert NoPendingTransfer();
        }
        if (msg.sender != transfer.recipient) {
            revert NotDesignatedRecipient();
        }

        address fromKeeper = transfer.fromKeeper;
        address recipient = transfer.recipient;
        delete pendingKeeperTransfers[snakeId];
        emit KeeperTransferRejected(snakeId, fromKeeper, recipient);
    }

    // Cancellation lets the current keeper withdraw an unaccepted proposal.
    // Without it, only the recipient could resolve a pending transfer.
    function cancelKeeperTransfer(string calldata snakeId) external {
        PendingKeeperTransfer storage transfer = pendingKeeperTransfers[snakeId];
        if (!transfer.exists) {
            revert NoPendingTransfer();
        }
        if (
            msg.sender != transfer.fromKeeper ||
            msg.sender != getCurrentKeeper(snakeId)
        ) {
            revert NotCurrentKeeper();
        }

        address fromKeeper = transfer.fromKeeper;
        address recipient = transfer.recipient;
        delete pendingKeeperTransfers[snakeId];
        emit KeeperTransferCancelled(snakeId, fromKeeper, recipient);
    }

    // Expose pending parties so the application can display available actions.
    // Without this query, the UI could only infer pending state from past events.
    function getPendingKeeperTransfer(
        string calldata snakeId
    ) external view returns (address fromKeeper, address recipient, bool pending) {
        getCurrentKeeper(snakeId);
        PendingKeeperTransfer storage transfer = pendingKeeperTransfers[snakeId];
        return (transfer.fromKeeper, transfer.recipient, transfer.exists);
    }
}
