// SPDX-License-Identifier: UNLICENSED
pragma solidity 0.8.28;

import {CertificateRegistry} from "./CertificateRegistry.sol";
import {SnakeRegistry} from "./SnakeRegistry.sol";

interface VmCertificateRegistryTest {
    function prank(address sender) external;

    function expectRevert(bytes4 selector) external;

    function expectRevert(bytes calldata revertData) external;
}

contract CertificateRegistryTest {
    VmCertificateRegistryTest private constant VM =
        VmCertificateRegistryTest(
            address(uint160(uint256(keccak256("hevm cheat code"))))
        );

    address private constant LAB001 = address(0x1AB001);
    address private constant LAB002 = address(0x1AB002);
    address private constant UNAUTHORIZED_LAB = address(0x1AB003);

    SnakeRegistry private snakeRegistry;
    CertificateRegistry private certificateRegistry;

    function setUp() public {
        snakeRegistry = new SnakeRegistry();
        snakeRegistry.registerSnake("SNAKE-001");

        certificateRegistry = new CertificateRegistry(address(snakeRegistry));
        certificateRegistry.authorizeLaboratory(LAB001);
        certificateRegistry.authorizeLaboratory(LAB002);
    }

    function testLabsIssueV1AndIssuerAppendsV2() public {
        bytes32 lab001V1Hash = keccak256("LAB001 PDF V1");
        bytes32 lab002V1Hash = keccak256("LAB002 PDF V1");
        bytes32 lab001V2Hash = keccak256("LAB001 PDF V2");

        VM.prank(LAB001);
        certificateRegistry.issueCertificate(
            "SNAKE-001",
            "SERIES-LAB001-001",
            "VERSION-LAB001-001-V1",
            lab001V1Hash
        );

        VM.prank(LAB002);
        certificateRegistry.issueCertificate(
            "SNAKE-001",
            "SERIES-LAB002-001",
            "VERSION-LAB002-001-V1",
            lab002V1Hash
        );

        VM.prank(LAB001);
        certificateRegistry.appendRevision(
            "SERIES-LAB001-001",
            "VERSION-LAB001-001-V2",
            lab001V2Hash
        );

        CertificateRegistry.VersionEvidence memory lab001V1 =
            certificateRegistry.getVersion("VERSION-LAB001-001-V1");
        CertificateRegistry.VersionEvidence memory lab001V2 =
            certificateRegistry.getVersion("VERSION-LAB001-001-V2");
        CertificateRegistry.VersionEvidence memory lab002V1 =
            certificateRegistry.getVersion("VERSION-LAB002-001-V1");

        require(lab001V1.versionNumber == 1, "LAB001 V1 must be version 1");
        require(lab001V1.fileHash == lab001V1Hash, "LAB001 V1 hash must persist");
        require(
            lab001V1.status == CertificateRegistry.VersionStatus.Superseded,
            "LAB001 V1 must be superseded"
        );

        require(lab001V2.versionNumber == 2, "LAB001 V2 must be version 2");
        require(lab001V2.fileHash == lab001V2Hash, "LAB001 V2 hash must match");
        require(lab001V2.issuer == LAB001, "Issuer must be the transaction sender");
        require(
            keccak256(bytes(lab001V2.previousVersionId)) ==
                keccak256(bytes("VERSION-LAB001-001-V1")),
            "LAB001 V2 must reference V1"
        );
        require(
            lab001V2.status == CertificateRegistry.VersionStatus.Current,
            "LAB001 V2 must be current"
        );

        require(lab002V1.versionNumber == 1, "LAB002 remains on V1");
        require(lab002V1.fileHash == lab002V1Hash, "LAB002 V1 hash must persist");
        require(
            lab002V1.status == CertificateRegistry.VersionStatus.Current,
            "LAB002 V1 must remain current"
        );

        CertificateRegistry.SeriesSummary memory series =
            certificateRegistry.getSeries("SERIES-LAB001-001");

        require(series.currentVersionNumber == 2, "Series current number must be 2");
        require(series.versionCount == 2, "Series must contain two versions");
        require(
            keccak256(bytes(series.currentVersionId)) ==
                keccak256(bytes("VERSION-LAB001-001-V2")),
            "Series current ID must be V2"
        );
        require(
            keccak256(
                bytes(
                    certificateRegistry.getSeriesVersionIdAt(
                        "SERIES-LAB001-001",
                        0
                    )
                )
            ) == keccak256(bytes("VERSION-LAB001-001-V1")),
            "History index zero must be V1"
        );
        require(
            keccak256(
                bytes(
                    certificateRegistry.getSeriesVersionIdAt(
                        "SERIES-LAB001-001",
                        1
                    )
                )
            ) == keccak256(bytes("VERSION-LAB001-001-V2")),
            "History index one must be V2"
        );
    }

    function testUnauthorizedLaboratoryCannotIssue() public {
        VM.expectRevert(CertificateRegistry.Unauthorized.selector);
        VM.prank(UNAUTHORIZED_LAB);
        certificateRegistry.issueCertificate(
            "SNAKE-001",
            "SERIES-UNAUTHORIZED",
            "VERSION-UNAUTHORIZED-V1",
            keccak256("PDF")
        );
    }

    function testAnotherLaboratoryCannotReviseSeries() public {
        VM.prank(LAB001);
        certificateRegistry.issueCertificate(
            "SNAKE-001",
            "SERIES-LAB001-001",
            "VERSION-LAB001-001-V1",
            keccak256("LAB001 PDF V1")
        );

        VM.expectRevert(
            abi.encodeWithSelector(
                CertificateRegistry.NotSeriesIssuer.selector,
                "SERIES-LAB001-001",
                LAB002
            )
        );
        VM.prank(LAB002);
        certificateRegistry.appendRevision(
            "SERIES-LAB001-001",
            "VERSION-LAB002-ATTEMPT",
            keccak256("altered PDF")
        );
    }

    function testOnlyAdministratorCanAuthorizeLaboratories() public {
        VM.expectRevert(CertificateRegistry.Unauthorized.selector);
        VM.prank(LAB001);
        certificateRegistry.authorizeLaboratory(UNAUTHORIZED_LAB);
    }

    function testDuplicateLaboratoryAuthorizationReverts() public {
        VM.expectRevert(
            abi.encodeWithSelector(
                CertificateRegistry.LaboratoryAlreadyAuthorized.selector,
                LAB001
            )
        );
        certificateRegistry.authorizeLaboratory(LAB001);
    }

    function testZeroAddressCannotBeAuthorized() public {
        VM.expectRevert(CertificateRegistry.ZeroAddress.selector);
        certificateRegistry.authorizeLaboratory(address(0));
    }

    function testVersionIdCannotBeReused() public {
        VM.prank(LAB001);
        certificateRegistry.issueCertificate(
            "SNAKE-001",
            "SERIES-LAB001-001",
            "VERSION-LAB001-001-V1",
            keccak256("LAB001 PDF V1")
        );

        VM.expectRevert(
            abi.encodeWithSelector(
                CertificateRegistry.VersionAlreadyExists.selector,
                "VERSION-LAB001-001-V1"
            )
        );
        VM.prank(LAB001);
        certificateRegistry.appendRevision(
            "SERIES-LAB001-001",
            "VERSION-LAB001-001-V1",
            keccak256("replacement PDF")
        );
    }

    function testCannotIssueForUnregisteredSnake() public {
        VM.expectRevert(SnakeRegistry.SnakeNotFound.selector);
        VM.prank(LAB001);
        certificateRegistry.issueCertificate(
            "SNAKE-UNKNOWN",
            "SERIES-UNKNOWN-SNAKE",
            "VERSION-UNKNOWN-SNAKE-V1",
            keccak256("PDF")
        );
    }

    function testReadOnlyVerificationDoesNotAppendVersion() public {
        VM.prank(LAB001);
        certificateRegistry.issueCertificate(
            "SNAKE-001",
            "SERIES-LAB001-001",
            "VERSION-LAB001-001-V1",
            keccak256("LAB001 PDF V1")
        );

        CertificateRegistry.VersionEvidence memory version =
            certificateRegistry.getVersion("VERSION-LAB001-001-V1");
        CertificateRegistry.SeriesSummary memory series =
            certificateRegistry.getSeries("SERIES-LAB001-001");

        require(
            version.fileHash == keccak256("LAB001 PDF V1"),
            "Read must return stored file hash"
        );
        require(series.versionCount == 1, "Read must not append a version");
        require(
            series.currentVersionNumber == 1,
            "Read must not change current version"
        );
    }
}
