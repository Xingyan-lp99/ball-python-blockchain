// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.34;

interface ISnakeRegistry {
  function managerOf(string calldata snakeId) external view returns (address);
  function instanceId() external view returns (bytes32);
}

contract CertificateRegistry {
  bytes32 public immutable instanceId;
  ISnakeRegistry public immutable snakeRegistry;
  address public immutable administrator;
  mapping(address => bool) public authorizedLaboratories;

  struct CertificateVersion {
    string snakeId;
    address issuer;
    uint256 version;
    bytes32 fileHash;
  }
  mapping(string => mapping(uint256 => CertificateVersion)) private records;

  error Unauthorized();
  error InvalidCertificate();
  error SnakeNotRegistered();
  error VersionAlreadyExists();
  event LaboratoryAuthorized(address indexed laboratory);
  event CertificateIssued(string certificateId, string snakeId, address indexed issuer, uint256 version, bytes32 fileHash);

  constructor(bytes32 deploymentInstanceId, address registry) {
    instanceId = deploymentInstanceId;
    snakeRegistry = ISnakeRegistry(registry);
    administrator = msg.sender;
  }

  function authorizeLaboratory(address laboratory) external {
    if (msg.sender != administrator) revert Unauthorized();
    if (laboratory == address(0)) revert InvalidCertificate();
    authorizedLaboratories[laboratory] = true;
    emit LaboratoryAuthorized(laboratory);
  }

  function issueV1(string calldata certificateId, string calldata snakeId, bytes32 fileHash) external {
    if (!authorizedLaboratories[msg.sender]) revert Unauthorized();
    if (bytes(certificateId).length == 0 || fileHash == bytes32(0)) revert InvalidCertificate();
    if (snakeRegistry.managerOf(snakeId) == address(0)) revert SnakeNotRegistered();
    if (records[certificateId][1].issuer != address(0)) revert VersionAlreadyExists();
    records[certificateId][1] = CertificateVersion(snakeId, msg.sender, 1, fileHash);
    emit CertificateIssued(certificateId, snakeId, msg.sender, 1, fileHash);
  }

  function getVersion(string calldata certificateId, uint256 version) external view returns (CertificateVersion memory) {
    return records[certificateId][version];
  }
}
