// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.34;

contract SnakeRegistry {
  bytes32 public immutable instanceId;
  mapping(string => address) public managerOf;

  error EmptySnakeId();
  error SnakeAlreadyRegistered();
  event SnakeRegistered(string snakeId, address indexed manager);

  constructor(bytes32 deploymentInstanceId) {
    instanceId = deploymentInstanceId;
  }

  function register(string calldata snakeId) external {
    bytes memory identifier = bytes(snakeId);
    bool hasContent;
    for (uint i = 0; i < identifier.length; i++) {
      if (uint8(identifier[i]) > 32) {
        hasContent = true;
        break;
      }
    }
    if (!hasContent) revert EmptySnakeId();
    if (managerOf[snakeId] != address(0)) revert SnakeAlreadyRegistered();
    managerOf[snakeId] = msg.sender;
    emit SnakeRegistered(snakeId, msg.sender);
  }
}
