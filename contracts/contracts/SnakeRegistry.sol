// SPDX-License-Identifier: UNLICENSED
pragma solidity 0.8.28;

/// @title Ball Python Identity and Initial Keeper Registry
/// @notice Registers a supplied snake ID and the address that registered it.
/// @dev Deploy this contract first. Pass its address to KeeperTransfers and
/// CertificateRegistry when deploying those contracts; their relative order
/// does not matter. No Python service or database is needed to call them.
/// Example: A registers SNAKE001, then uses KeeperTransfers to propose B;
/// only B's acceptance there changes the current management authority.
/// This contract retains A as the initial keeper even after that acceptance.
/// Profiles, photographs, husbandry records, and original PDFs remain off-chain.
/// An ID is unique within this registry, not proof of a unique physical animal.
contract SnakeRegistry {
    // Historical name: this mapping stores initial keepers, never transfer results.
    mapping(string => address) private currentKeepers;

    error EmptySnakeId();
    error SnakeAlreadyRegistered();
    error SnakeNotFound();

    event SnakeRegistered(string snakeId, address keeper);

    // Demo step 1: register an identifier and its initial keeper.
    // Without this operation, certificates and transfers have no registered snake.
    // The caller supplies the ID; this contract does not generate or normalize it.
    // Any address may register a nonempty unused ID. Case and whitespace matter.
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

    // Read the initial keeper and reject IDs that have never been registered.
    // CertificateRegistry uses this query only to check that a snake exists.
    // Current management permissions must query KeeperTransfers.getCurrentKeeper.
    // Removing this query breaks existence checks and initial-keeper lookup.
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
