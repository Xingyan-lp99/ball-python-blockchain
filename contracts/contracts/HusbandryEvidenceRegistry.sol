// SPDX-License-Identifier: UNLICENSED
pragma solidity 0.8.28;

interface IHusbandrySnakeRegistry {
    function getCurrentKeeper(
        string calldata snakeId
    ) external view returns (address);
}

contract HusbandryEvidenceRegistry {
    enum RecordCategory {
        Growth,
        Shedding,
        Feeding,
        Health
    }

    struct RecordEvidence {
        string snakeId;
        string recordId;
        RecordCategory category;
        address author;
        bytes32 contentHash;
        uint256 versionNumber;
        bool deleted;
        bool exists;
    }

    struct RecordReference {
        string recordId;
        RecordCategory category;
    }

    IHusbandrySnakeRegistry public immutable snakeRegistry;

    mapping(bytes32 => RecordEvidence) private recordsByKey;
    mapping(string => RecordReference[]) private recordReferencesBySnake;

    error ZeroAddress();
    error EmptyRecordId();
    error RecordAlreadyExists();
    error RecordNotFound();
    error RecordDeleted();
    error NotCurrentKeeper();
    error NotRecordAuthor();
    error RecordIndexOutOfBounds();

    event HusbandryRecordAdded(
        string indexed snakeId,
        string indexed recordId,
        RecordCategory category,
        address indexed author,
        bytes32 contentHash
    );

    event HusbandryRecordUpdated(
        string indexed snakeId,
        string indexed recordId,
        address indexed author,
        uint256 versionNumber,
        bytes32 previousHash,
        bytes32 newHash
    );

    event HusbandryRecordDeleted(
        string indexed snakeId,
        string indexed recordId,
        address indexed author,
        bytes32 contentHash
    );

    constructor(address snakeRegistryAddress) {
        if (snakeRegistryAddress == address(0)) {
            revert ZeroAddress();
        }

        snakeRegistry = IHusbandrySnakeRegistry(snakeRegistryAddress);
    }

    function addRecordEvidence(
        string calldata snakeId,
        string calldata recordId,
        RecordCategory category,
        bytes32 contentHash
    ) external {
        if (bytes(recordId).length == 0) {
            revert EmptyRecordId();
        }

        bytes32 recordKey = _recordKey(snakeId, recordId, category);
        if (recordsByKey[recordKey].exists) {
            revert RecordAlreadyExists();
        }

        address currentKeeper = snakeRegistry.getCurrentKeeper(snakeId);
        if (msg.sender != currentKeeper) {
            revert NotCurrentKeeper();
        }

        recordsByKey[recordKey] = RecordEvidence({
            snakeId: snakeId,
            recordId: recordId,
            category: category,
            author: msg.sender,
            contentHash: contentHash,
            versionNumber: 1,
            deleted: false,
            exists: true
        });

        recordReferencesBySnake[snakeId].push(
            RecordReference({recordId: recordId, category: category})
        );

        emit HusbandryRecordAdded(
            snakeId,
            recordId,
            category,
            msg.sender,
            contentHash
        );
    }

    function updateRecordEvidence(
        string calldata snakeId,
        string calldata recordId,
        RecordCategory category,
        bytes32 newContentHash
    ) external {
        RecordEvidence storage record = recordsByKey[
            _recordKey(snakeId, recordId, category)
        ];

        if (!record.exists) {
            revert RecordNotFound();
        }

        if (record.deleted) {
            revert RecordDeleted();
        }

        address currentKeeper = snakeRegistry.getCurrentKeeper(record.snakeId);
        if (msg.sender != currentKeeper) {
            revert NotCurrentKeeper();
        }

        if (msg.sender != record.author) {
            revert NotRecordAuthor();
        }

        bytes32 previousHash = record.contentHash;
        record.contentHash = newContentHash;
        record.versionNumber += 1;

        emit HusbandryRecordUpdated(
            record.snakeId,
            recordId,
            record.author,
            record.versionNumber,
            previousHash,
            newContentHash
        );
    }

    function deleteRecordEvidence(
        string calldata snakeId,
        string calldata recordId,
        RecordCategory category
    ) external {
        RecordEvidence storage record = recordsByKey[
            _recordKey(snakeId, recordId, category)
        ];

        if (!record.exists) {
            revert RecordNotFound();
        }

        if (record.deleted) {
            revert RecordDeleted();
        }

        address currentKeeper = snakeRegistry.getCurrentKeeper(record.snakeId);
        if (msg.sender != currentKeeper) {
            revert NotCurrentKeeper();
        }

        if (msg.sender != record.author) {
            revert NotRecordAuthor();
        }

        record.deleted = true;

        emit HusbandryRecordDeleted(
            record.snakeId,
            recordId,
            record.author,
            record.contentHash
        );
    }

    function getRecordEvidence(
        string calldata snakeId,
        string calldata recordId,
        RecordCategory category
    ) external view returns (RecordEvidence memory evidence) {
        bytes32 recordKey = _recordKey(snakeId, recordId, category);
        if (!recordsByKey[recordKey].exists) {
            revert RecordNotFound();
        }

        return recordsByKey[recordKey];
    }

    function getSnakeRecordCount(
        string calldata snakeId
    ) external view returns (uint256 count) {
        snakeRegistry.getCurrentKeeper(snakeId);
        return recordReferencesBySnake[snakeId].length;
    }

    function getSnakeRecordAt(
        string calldata snakeId,
        uint256 index
    ) external view returns (RecordReference memory recordReference) {
        snakeRegistry.getCurrentKeeper(snakeId);

        if (index >= recordReferencesBySnake[snakeId].length) {
            revert RecordIndexOutOfBounds();
        }

        return recordReferencesBySnake[snakeId][index];
    }

    function _recordKey(
        string memory snakeId,
        string memory recordId,
        RecordCategory category
    ) private pure returns (bytes32) {
        return keccak256(abi.encode(snakeId, recordId, category));
    }
}
