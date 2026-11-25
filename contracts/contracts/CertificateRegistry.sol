// SPDX-License-Identifier: UNLICENSED
pragma solidity 0.8.28;

// Only snake existence is needed here; certificate authority belongs to laboratories.
interface ISnakeRegistry {
    function getCurrentKeeper(
        string calldata snakeId
    ) external view returns (address);
}

/// @title Ball Python Laboratory Certificate Evidence
/// @notice Laboratory permissions and append-only certificate evidence.
/// @dev The application supplies SHA-256 of the original PDF bytes as fileHash.
/// The contract stores that digest without validating the file or hash algorithm.
/// Deploy after SnakeRegistry and supply its address, not KeeperTransfers.
/// The deployer authorizes laboratories; each laboratory controls its own series.
/// Example: LAB001 and LAB002 issue independent V1 reports for SNAKE001.
/// LAB001 appends V2 to its series; its V1 becomes Superseded but stays readable.
/// Keeper transfers do not change issuers, report history, or laboratory rights.
/// Original PDFs and report contents stay off-chain. A matching digest supports
/// byte-level integrity comparison, not the biological truth of a report.
/// This implementation has no certificate revocation or laboratory removal operation.
contract CertificateRegistry {
    enum VersionStatus {
        None,
        Current,
        Superseded
    }

    struct VersionEvidence {
        string snakeId;
        string seriesId;
        string versionId;
        uint256 versionNumber;
        string previousVersionId;
        address issuer;
        bytes32 fileHash;
        VersionStatus status;
    }

    struct SeriesSummary {
        string snakeId;
        address issuer;
        string currentVersionId;
        uint256 currentVersionNumber;
        uint256 versionCount;
    }

    struct SeriesData {
        string snakeId;
        address issuer;
        string currentVersionId;
        uint256 currentVersionNumber;
        uint256 versionCount;
        bool exists;
    }

    // The deploying administrator remains fixed; the public getter is unchanged.
    address public immutable administrator;
    ISnakeRegistry public immutable snakeRegistry;

    mapping(address => bool) private authorizedLaboratories;
    mapping(string => SeriesData) private seriesById;
    mapping(string => VersionEvidence) private versionsById;
    mapping(string => bool) private usedSeriesIds;
    mapping(string => bool) private usedVersionIds;
    mapping(string => string[]) private versionIdsBySeries;

    error ZeroAddress();
    error Unauthorized();
    error LaboratoryAlreadyAuthorized(address laboratory);
    error EmptySeriesId();
    error EmptyVersionId();
    error SeriesAlreadyExists(string seriesId);
    error VersionAlreadyExists(string versionId);
    error SeriesNotFound(string seriesId);
    error VersionNotFound(string versionId);
    error VersionIndexOutOfBounds(string seriesId, uint256 index);
    error NotSeriesIssuer(string seriesId, address caller);
    error InvalidCurrentVersion(string seriesId, string versionId);

    event LaboratoryAuthorized(address laboratory);

    // Indexed string fields contain Keccak topics, not readable identifiers.
    // Keep the submitted identifiers off-chain and read full evidence with getVersion.
    event CertificateIssued(
        string indexed seriesId,
        string indexed versionId,
        string snakeId,
        address indexed issuer,
        uint256 versionNumber,
        bytes32 fileHash
    );

    event CertificateRevised(
        string indexed seriesId,
        string indexed previousVersionId,
        string indexed versionId,
        address issuer,
        uint256 versionNumber,
        bytes32 fileHash
    );

    // Deployment fixes both the administrator and the snake registration source.
    // Without this setup, laboratory grants and snake-existence checks lack authority.
    // Only the zero address is rejected here; deployment must verify the registry.
    constructor(address snakeRegistryAddress) {
        if (snakeRegistryAddress == address(0)) {
            revert ZeroAddress();
        }

        administrator = msg.sender;
        snakeRegistry = ISnakeRegistry(snakeRegistryAddress);
    }

    // Setup step: only the deploying administrator may grant issuance permission.
    // Without this operation, no laboratory could issue an initial certificate.
    function authorizeLaboratory(address laboratory) external {
        if (msg.sender != administrator) {
            revert Unauthorized();
        }

        if (laboratory == address(0)) {
            revert ZeroAddress();
        }

        if (authorizedLaboratories[laboratory]) {
            revert LaboratoryAlreadyAuthorized(laboratory);
        }

        authorizedLaboratories[laboratory] = true;
        emit LaboratoryAuthorized(laboratory);
    }

    // Read issuance permission without changing it, for setup and application checks.
    // Without this query, callers lose a direct view of the authorization mapping.
    function isAuthorizedLaboratory(
        address laboratory
    ) external view returns (bool authorized) {
        return authorizedLaboratories[laboratory];
    }

    // Report step: an authorized laboratory supplies snake/series/version IDs and hash.
    // Store V1 with msg.sender as issuer and emit its evidence; return no value.
    // Without this operation, neither an initial report nor its later revisions exist.
    function issueCertificate(
        string calldata snakeId,
        string calldata seriesId,
        string calldata versionId,
        bytes32 fileHash
    ) external {
        if (!authorizedLaboratories[msg.sender]) {
            revert Unauthorized();
        }

        if (bytes(seriesId).length == 0) {
            revert EmptySeriesId();
        }

        if (bytes(versionId).length == 0) {
            revert EmptyVersionId();
        }

        if (usedSeriesIds[seriesId]) {
            revert SeriesAlreadyExists(seriesId);
        }

        if (usedVersionIds[versionId]) {
            revert VersionAlreadyExists(versionId);
        }

        snakeRegistry.getCurrentKeeper(snakeId);

        usedSeriesIds[seriesId] = true;
        usedVersionIds[versionId] = true;

        seriesById[seriesId] = SeriesData({
            snakeId: snakeId,
            issuer: msg.sender,
            currentVersionId: versionId,
            currentVersionNumber: 1,
            versionCount: 1,
            exists: true
        });

        versionsById[versionId] = VersionEvidence({
            snakeId: snakeId,
            seriesId: seriesId,
            versionId: versionId,
            versionNumber: 1,
            previousVersionId: "",
            issuer: msg.sender,
            fileHash: fileHash,
            status: VersionStatus.Current
        });

        versionIdsBySeries[seriesId].push(versionId);

        emit CertificateIssued(
            seriesId,
            versionId,
            snakeId,
            msg.sender,
            1,
            fileHash
        );
    }

    /// @dev Appends to the latest version; the predecessor is selected on-chain.
    // Revision step: only the original series issuer may add a new version and hash.
    // Previous evidence remains stored; its status changes to Superseded.
    // Without this operation, a laboratory cannot append a traceable correction.
    function appendRevision(
        string calldata seriesId,
        string calldata versionId,
        bytes32 fileHash
    ) external {
        SeriesData storage series = seriesById[seriesId];

        if (!series.exists) {
            revert SeriesNotFound(seriesId);
        }

        if (series.issuer != msg.sender) {
            revert NotSeriesIssuer(seriesId, msg.sender);
        }

        if (bytes(versionId).length == 0) {
            revert EmptyVersionId();
        }

        if (usedVersionIds[versionId]) {
            revert VersionAlreadyExists(versionId);
        }

        string memory previousVersionId = series.currentVersionId;
        VersionEvidence storage previousVersion = versionsById[
            previousVersionId
        ];

        if (
            previousVersion.status != VersionStatus.Current ||
            previousVersion.versionNumber != series.currentVersionNumber
        ) {
            revert InvalidCurrentVersion(seriesId, previousVersionId);
        }

        previousVersion.status = VersionStatus.Superseded;

        uint256 newVersionNumber = series.currentVersionNumber + 1;

        usedVersionIds[versionId] = true;

        versionsById[versionId] = VersionEvidence({
            snakeId: series.snakeId,
            seriesId: seriesId,
            versionId: versionId,
            versionNumber: newVersionNumber,
            previousVersionId: previousVersionId,
            issuer: msg.sender,
            fileHash: fileHash,
            status: VersionStatus.Current
        });

        series.currentVersionId = versionId;
        series.currentVersionNumber = newVersionNumber;
        series.versionCount += 1;
        versionIdsBySeries[seriesId].push(versionId);

        emit CertificateRevised(
            seriesId,
            previousVersionId,
            versionId,
            msg.sender,
            newVersionNumber,
            fileHash
        );
    }

    // Viewing step: return stored evidence, including historical version status.
    // Without this query, callers cannot directly inspect a version's hash and issuer.
    function getVersion(
        string calldata versionId
    ) external view returns (VersionEvidence memory evidence) {
        if (!usedVersionIds[versionId]) {
            revert VersionNotFound(versionId);
        }

        return versionsById[versionId];
    }

    // Viewing step: return the series issuer, current version, and version count.
    // Without this query, callers lack a direct summary of the latest report version.
    function getSeries(
        string calldata seriesId
    ) external view returns (SeriesSummary memory summary) {
        SeriesData storage series = seriesById[seriesId];

        if (!series.exists) {
            revert SeriesNotFound(seriesId);
        }

        return
            SeriesSummary({
                snakeId: series.snakeId,
                issuer: series.issuer,
                currentVersionId: series.currentVersionId,
                currentVersionNumber: series.currentVersionNumber,
                versionCount: series.versionCount
            });
    }

    // History step: return a version ID by zero-based index within its series.
    // Combine with getSeries and getVersion to inspect retained report history.
    // Without this query, callers would need another index, such as event logs.
    function getSeriesVersionIdAt(
        string calldata seriesId,
        uint256 index
    ) external view returns (string memory versionId) {
        if (!seriesById[seriesId].exists) {
            revert SeriesNotFound(seriesId);
        }

        if (index >= versionIdsBySeries[seriesId].length) {
            revert VersionIndexOutOfBounds(seriesId, index);
        }

        return versionIdsBySeries[seriesId][index];
    }
}
