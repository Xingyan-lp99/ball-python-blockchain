// SPDX-License-Identifier: UNLICENSED
pragma solidity 0.8.28;

contract SnakeRegistry {
    mapping(string => address) private currentKeepers;

    error EmptySnakeId();
    error SnakeAlreadyRegistered();
    error SnakeNotFound();

    event SnakeRegistered(string snakeId, address keeper);

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
}