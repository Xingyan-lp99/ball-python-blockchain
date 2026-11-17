// SPDX-License-Identifier: UNLICENSED
pragma solidity 0.8.28;

interface ISnakeRegistry {
    function getCurrentKeeper(
        string calldata snakeId
    ) external view returns (address);
}

/// @notice Laboratory permissions and append-only certificate evidence.
/// @dev The application supplies SHA-256 of the original PDF bytes as fileHash.
/// The contract stores that digest without validating the file or hash algorithm.
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

    constructor(address snakeRegistryAddress) {
        if (snakeRegistryAddress == address(0)) {
            revert ZeroAddress();
        }

        administrator = msg.sender;
        snakeRegistry = ISnakeRegistry(snakeRegistryAddress);
    }

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

    function isAuthorizedLaboratory(
        address laboratory
    ) external view returns (bool authorized) {
        return authorizedLaboratories[laboratory];
    }

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

    function getVersion(
        string calldata versionId
    ) external view returns (VersionEvidence memory evidence) {
        if (!usedVersionIds[versionId]) {
            revert VersionNotFound(versionId);
        }

        return versionsById[versionId];
    }

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
