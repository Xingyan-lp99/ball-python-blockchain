// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.34;

import {Test} from "forge-std/Test.sol";
import {SnakeRegistry} from "./SnakeRegistry.sol";
import {CertificateRegistry} from "./CertificateRegistry.sol";

contract CertificateRegistryTest is Test {
  SnakeRegistry snakes;
  CertificateRegistry certificates;
  address laboratory = address(0x1AB001);
  bytes32 fileHash = sha256("TEST ONLY PDF");
  event CertificateIssued(string certificateId, string snakeId, address indexed issuer, uint256 version, bytes32 fileHash);

  function setUp() public {
    snakes = new SnakeRegistry(bytes32(uint256(1)));
    snakes.register("TEST-S001");
    certificates = new CertificateRegistry(bytes32(uint256(2)), address(snakes));
    certificates.authorizeLaboratory(laboratory);
  }

  function test_AuthorizedIssueBindsCallerAndEmitsEvidence() public {
    vm.expectEmit(false, true, false, true);
    emit CertificateIssued("TEST-C001", "TEST-S001", laboratory, 1, fileHash);
    vm.prank(laboratory);
    certificates.issueV1("TEST-C001", "TEST-S001", fileHash);
    CertificateRegistry.CertificateVersion memory record = certificates.getVersion("TEST-C001", 1);
    assertEq(record.snakeId, "TEST-S001");
    assertEq(record.issuer, laboratory);
    assertEq(record.version, 1);
    assertEq(record.fileHash, fileHash);
  }

  function test_UnauthorizedIssuerRejected() public {
    vm.expectRevert(CertificateRegistry.Unauthorized.selector);
    certificates.issueV1("TEST-C001", "TEST-S001", fileHash);
  }

  function test_OnlyAdministratorCanAuthorize() public {
    vm.prank(laboratory);
    vm.expectRevert(CertificateRegistry.Unauthorized.selector);
    certificates.authorizeLaboratory(address(0x1234));
  }

  function test_UnknownSnakeRejected() public {
    vm.prank(laboratory);
    vm.expectRevert(CertificateRegistry.SnakeNotRegistered.selector);
    certificates.issueV1("TEST-C001", "missing", fileHash);
  }

  function test_V1CannotBeOverwritten() public {
    bytes32 modifiedHash = sha256("different");
    vm.startPrank(laboratory);
    certificates.issueV1("TEST-C001", "TEST-S001", fileHash);
    vm.expectRevert(CertificateRegistry.VersionAlreadyExists.selector);
    certificates.issueV1("TEST-C001", "TEST-S001", modifiedHash);
    vm.stopPrank();
    assertEq(certificates.getVersion("TEST-C001", 1).fileHash, fileHash);
  }

  function test_DifferentCertificatesForSameSnake() public {
    vm.startPrank(laboratory);
    certificates.issueV1("TEST-C001", "TEST-S001", fileHash);
    certificates.issueV1("TEST-C002", "TEST-S001", fileHash);
    vm.stopPrank();
    assertEq(certificates.getVersion("TEST-C002", 1).issuer, laboratory);
  }

  function test_InvalidCertificateRejected() public {
    vm.prank(laboratory);
    vm.expectRevert(CertificateRegistry.InvalidCertificate.selector);
    certificates.issueV1("", "TEST-S001", fileHash);
  }

  function test_NoV2RecordExists() public view {
    assertEq(certificates.getVersion("TEST-C001", 2).version, 0);
  }
}
