// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.34;

import {ISnakeRegistry} from "./CertificateRegistry.sol";

contract VersionedCertificateRegistry {
  bytes32 public immutable instanceId;
  ISnakeRegistry public immutable snakeRegistry;
  address public immutable administrator;
  mapping(address => bool) public authorizedLaboratories;
  mapping(string => uint256) public latestVersion;
  struct CertificateVersion { string snakeId; address issuer; uint256 version; bytes32 fileHash; }
  mapping(string => mapping(uint256 => CertificateVersion)) private records;

  error Unauthorized();
  error NotOriginalIssuer();
  error SeriesImmutable();
  error InvalidVersion();
  error InvalidCertificate();
  error SnakeNotRegistered();
  event LaboratoryAuthorization(address indexed laboratory, bool authorized);
  event CertificateIssued(string certificateId, string snakeId, address indexed issuer, uint256 version, bytes32 fileHash);

  constructor(bytes32 deploymentInstanceId, address registry) {
    instanceId = deploymentInstanceId;
    snakeRegistry = ISnakeRegistry(registry);
    administrator = msg.sender;
  }

  function setLaboratoryAuthorization(address laboratory, bool authorized) public {
    if (msg.sender != administrator) revert Unauthorized();
    if (laboratory == address(0)) revert InvalidCertificate();
    authorizedLaboratories[laboratory] = authorized;
    emit LaboratoryAuthorization(laboratory, authorized);
  }

  function authorizeLaboratory(address laboratory) external {
    setLaboratoryAuthorization(laboratory, true);
  }

  function issueVersion(string calldata certificateId, string calldata snakeId, uint256 version, bytes32 fileHash) external {
    if (!authorizedLaboratories[msg.sender]) revert Unauthorized();
    if (bytes(certificateId).length == 0 || fileHash == bytes32(0)) revert InvalidCertificate();
    uint256 latest = latestVersion[certificateId];
    if (version != latest + 1) revert InvalidVersion();
    if (latest == 0) {
      if (snakeRegistry.managerOf(snakeId) == address(0)) revert SnakeNotRegistered();
    } else {
      CertificateVersion storage original = records[certificateId][1];
      if (msg.sender != original.issuer) revert NotOriginalIssuer();
      if (keccak256(bytes(snakeId)) != keccak256(bytes(original.snakeId))) revert SeriesImmutable();
    }
    records[certificateId][version] = CertificateVersion(snakeId, msg.sender, version, fileHash);
    latestVersion[certificateId] = version;
    emit CertificateIssued(certificateId, snakeId, msg.sender, version, fileHash);
  }

  function getVersion(string calldata certificateId, uint256 version) external view returns (CertificateVersion memory) {
    return records[certificateId][version];
  }
}
