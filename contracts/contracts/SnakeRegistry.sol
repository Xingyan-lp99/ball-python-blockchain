// SPDX-License-Identifier: UNLICENSED
pragma solidity 0.8.28;

contract SnakeRegistry {
    struct PendingKeeperTransfer {
        address fromKeeper;
        address recipient;
        bool exists;
    }

    mapping(string => address) private currentKeepers;
    mapping(string => PendingKeeperTransfer) private pendingKeeperTransfers;

    error EmptySnakeId();
    error SnakeAlreadyRegistered();
    error SnakeNotFound();
    error ZeroAddress();
    error SameKeeper();
    error TransferAlreadyPending();
    error NoPendingTransfer();
    error NotCurrentKeeper();
    error NotDesignatedRecipient();
    error InvalidTransferState();

    event SnakeRegistered(string snakeId, address keeper);
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

    // Demo step 1: register an identifier and its initial keeper.
    // Without this operation, certificates and transfers have no registered snake.
    function registerSnake(string calldata snakeId) external {
        if (bytes(snakeId).length == 0) {
            revert EmptySnakeId();
        }

        if (currentKeepers[snakeId] != address(0)) {
            revert SnakeAlreadyRegistered();
        }

        currentKeepers[snakeId] = msg.sender;

        emit SnakeRegistered(snakeId, msg.sender);
    }

    // Read keeper state for registration checks and later permission checks.
    // Without this query, callers cannot retrieve the confirmed keeper here.
    function getCurrentKeeper(
        string calldata snakeId
    ) external view returns (address) {
        address keeper = currentKeepers[snakeId];

        if (keeper == address(0)) {
            revert SnakeNotFound();
        }

        return keeper;
    }

    function initiateKeeperTransfer(
        string calldata snakeId,
        address recipient
    ) external {
        address currentKeeper = currentKeepers[snakeId];

        if (currentKeeper == address(0)) {
            revert SnakeNotFound();
        }

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

    function acceptKeeperTransfer(string calldata snakeId) external {
        PendingKeeperTransfer storage transfer = pendingKeeperTransfers[
            snakeId
        ];

        if (!transfer.exists) {
            revert NoPendingTransfer();
        }

        if (msg.sender != transfer.recipient) {
            revert NotDesignatedRecipient();
        }

        if (currentKeepers[snakeId] != transfer.fromKeeper) {
            revert InvalidTransferState();
        }

        address previousKeeper = transfer.fromKeeper;
        address newKeeper = transfer.recipient;

        currentKeepers[snakeId] = newKeeper;

        emit KeeperTransferAccepted(snakeId, previousKeeper, newKeeper);
        delete pendingKeeperTransfers[snakeId];
    }

    function rejectKeeperTransfer(string calldata snakeId) external {
        PendingKeeperTransfer storage transfer = pendingKeeperTransfers[
            snakeId
        ];

        if (!transfer.exists) {
            revert NoPendingTransfer();
        }

        if (msg.sender != transfer.recipient) {
            revert NotDesignatedRecipient();
        }

        emit KeeperTransferRejected(
            snakeId,
            transfer.fromKeeper,
            transfer.recipient
        );

        delete pendingKeeperTransfers[snakeId];
    }

    function cancelKeeperTransfer(string calldata snakeId) external {
        PendingKeeperTransfer storage transfer = pendingKeeperTransfers[
            snakeId
        ];

        if (!transfer.exists) {
            revert NoPendingTransfer();
        }

        if (msg.sender != transfer.fromKeeper) {
            revert NotCurrentKeeper();
        }

        emit KeeperTransferCancelled(
            snakeId,
            transfer.fromKeeper,
            transfer.recipient
        );

        delete pendingKeeperTransfers[snakeId];
    }

    function getPendingKeeperTransfer(
        string calldata snakeId
    )
        external
        view
        returns (address fromKeeper, address recipient, bool pending)
    {
        if (currentKeepers[snakeId] == address(0)) {
            revert SnakeNotFound();
        }

        PendingKeeperTransfer storage transfer = pendingKeeperTransfers[
            snakeId
        ];

        return (transfer.fromKeeper, transfer.recipient, transfer.exists);
    }
}
