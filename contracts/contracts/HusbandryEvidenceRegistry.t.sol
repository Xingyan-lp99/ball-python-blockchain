// SPDX-License-Identifier: UNLICENSED
pragma solidity 0.8.28;

import {HusbandryEvidenceRegistry} from "./HusbandryEvidenceRegistry.sol";
import {SnakeRegistry} from "./SnakeRegistry.sol";

interface VmHusbandryEvidenceRegistryTest {
    function prank(address sender) external;

    function expectRevert(bytes4 selector) external;
}

contract HusbandryEvidenceRegistryTest {
    VmHusbandryEvidenceRegistryTest private constant VM =
        VmHusbandryEvidenceRegistryTest(
            address(uint160(uint256(keccak256("hevm cheat code"))))
        );

    address private constant BREEDER = address(0xB001);
    address private constant BUYER = address(0xB002);

    SnakeRegistry private snakeRegistry;
    HusbandryEvidenceRegistry private evidenceRegistry;

    function setUp() public {
        snakeRegistry = new SnakeRegistry();

        VM.prank(BREEDER);
        snakeRegistry.registerSnake("SNAKE001");

        evidenceRegistry = new HusbandryEvidenceRegistry(
            address(snakeRegistry)
        );
    }

    function testNewKeeperCanAddButCannotChangeFormerKeepersRecord() public {
        bytes32 breederHash = sha256(bytes("breeder feeding record"));
        bytes32 buyerHash = sha256(bytes("buyer feeding record"));
        bytes32 changedBreederHash = sha256(bytes("changed breeder record"));

        VM.prank(BREEDER);
        evidenceRegistry.addRecordEvidence(
            "SNAKE001",
            "RECORD-BREEDER-001",
            HusbandryEvidenceRegistry.RecordCategory.Feeding,
            breederHash
        );

        VM.prank(BREEDER);
        snakeRegistry.initiateKeeperTransfer("SNAKE001", BUYER);

        VM.prank(BUYER);
        snakeRegistry.acceptKeeperTransfer("SNAKE001");

        VM.prank(BUYER);
        evidenceRegistry.addRecordEvidence(
            "SNAKE001",
            "RECORD-BUYER-001",
            HusbandryEvidenceRegistry.RecordCategory.Feeding,
            buyerHash
        );

        VM.expectRevert(HusbandryEvidenceRegistry.NotRecordAuthor.selector);
        VM.prank(BUYER);
        evidenceRegistry.updateRecordEvidence(
            "SNAKE001",
            "RECORD-BREEDER-001",
            HusbandryEvidenceRegistry.RecordCategory.Feeding,
            changedBreederHash
        );

        VM.expectRevert(HusbandryEvidenceRegistry.NotRecordAuthor.selector);
        VM.prank(BUYER);
        evidenceRegistry.deleteRecordEvidence(
            "SNAKE001",
            "RECORD-BREEDER-001",
            HusbandryEvidenceRegistry.RecordCategory.Feeding
        );

        HusbandryEvidenceRegistry.RecordEvidence memory breederRecord =
            evidenceRegistry.getRecordEvidence(
                "SNAKE001",
                "RECORD-BREEDER-001",
                HusbandryEvidenceRegistry.RecordCategory.Feeding
            );
        HusbandryEvidenceRegistry.RecordEvidence memory buyerRecord =
            evidenceRegistry.getRecordEvidence(
                "SNAKE001",
                "RECORD-BUYER-001",
                HusbandryEvidenceRegistry.RecordCategory.Feeding
            );

        require(breederRecord.author == BREEDER, "Original author must persist");
        require(
            breederRecord.contentHash == breederHash,
            "Former keeper record hash must remain unchanged"
        );
        require(!breederRecord.deleted, "Former keeper record must remain active");
        require(buyerRecord.author == BUYER, "New record author must be buyer");
        require(buyerRecord.contentHash == buyerHash, "Buyer hash must be stored");
    }

    function testFormerKeeperCannotChangeOwnRecordAfterTransfer() public {
        bytes32 breederHash = sha256(bytes("breeder growth record"));
        bytes32 changedHash = sha256(bytes("former keeper change"));

        VM.prank(BREEDER);
        evidenceRegistry.addRecordEvidence(
            "SNAKE001",
            "RECORD-BREEDER-001",
            HusbandryEvidenceRegistry.RecordCategory.Growth,
            breederHash
        );

        VM.prank(BREEDER);
        snakeRegistry.initiateKeeperTransfer("SNAKE001", BUYER);

        VM.prank(BUYER);
        snakeRegistry.acceptKeeperTransfer("SNAKE001");

        VM.expectRevert(HusbandryEvidenceRegistry.NotCurrentKeeper.selector);
        VM.prank(BREEDER);
        evidenceRegistry.updateRecordEvidence(
            "SNAKE001",
            "RECORD-BREEDER-001",
            HusbandryEvidenceRegistry.RecordCategory.Growth,
            changedHash
        );

        VM.expectRevert(HusbandryEvidenceRegistry.NotCurrentKeeper.selector);
        VM.prank(BREEDER);
        evidenceRegistry.deleteRecordEvidence(
            "SNAKE001",
            "RECORD-BREEDER-001",
            HusbandryEvidenceRegistry.RecordCategory.Growth
        );
    }

    function testCurrentOriginalAuthorCanUpdateOwnRecord() public {
        bytes32 firstHash = sha256(bytes("first value"));
        bytes32 secondHash = sha256(bytes("updated value"));

        VM.prank(BREEDER);
        evidenceRegistry.addRecordEvidence(
            "SNAKE001",
            "RECORD-BREEDER-001",
            HusbandryEvidenceRegistry.RecordCategory.Health,
            firstHash
        );

        VM.prank(BREEDER);
        evidenceRegistry.updateRecordEvidence(
            "SNAKE001",
            "RECORD-BREEDER-001",
            HusbandryEvidenceRegistry.RecordCategory.Health,
            secondHash
        );

        HusbandryEvidenceRegistry.RecordEvidence memory record =
            evidenceRegistry.getRecordEvidence(
                "SNAKE001",
                "RECORD-BREEDER-001",
                HusbandryEvidenceRegistry.RecordCategory.Health
            );

        require(record.author == BREEDER, "Update must preserve original author");
        require(record.contentHash == secondHash, "Latest hash must be stored");
        require(record.versionNumber == 2, "Update must increment version");
    }

    function testCurrentOriginalAuthorCanDeleteOwnRecord() public {
        bytes32 recordHash = sha256(bytes("shedding record"));

        VM.prank(BREEDER);
        evidenceRegistry.addRecordEvidence(
            "SNAKE001",
            "RECORD-BREEDER-001",
            HusbandryEvidenceRegistry.RecordCategory.Shedding,
            recordHash
        );

        VM.prank(BREEDER);
        evidenceRegistry.deleteRecordEvidence(
            "SNAKE001",
            "RECORD-BREEDER-001",
            HusbandryEvidenceRegistry.RecordCategory.Shedding
        );

        HusbandryEvidenceRegistry.RecordEvidence memory record =
            evidenceRegistry.getRecordEvidence(
                "SNAKE001",
                "RECORD-BREEDER-001",
                HusbandryEvidenceRegistry.RecordCategory.Shedding
            );

        require(record.deleted, "Deletion must be recorded on chain");
        require(record.author == BREEDER, "Deletion must preserve author");
        require(
            evidenceRegistry.getSnakeRecordCount("SNAKE001") == 1,
            "Deleted evidence must remain in history"
        );
    }

    function testNonKeeperCannotAddRecord() public {
        bytes32 recordHash = sha256(bytes("buyer record"));

        VM.expectRevert(HusbandryEvidenceRegistry.NotCurrentKeeper.selector);
        VM.prank(BUYER);
        evidenceRegistry.addRecordEvidence(
            "SNAKE001",
            "RECORD-BUYER-001",
            HusbandryEvidenceRegistry.RecordCategory.Feeding,
            recordHash
        );
    }

    function testRecordIdCannotBeReused() public {
        bytes32 firstHash = sha256(bytes("first record"));
        bytes32 replacementHash = sha256(bytes("replacement record"));

        VM.prank(BREEDER);
        evidenceRegistry.addRecordEvidence(
            "SNAKE001",
            "RECORD-001",
            HusbandryEvidenceRegistry.RecordCategory.Feeding,
            firstHash
        );

        VM.expectRevert(HusbandryEvidenceRegistry.RecordAlreadyExists.selector);
        VM.prank(BREEDER);
        evidenceRegistry.addRecordEvidence(
            "SNAKE001",
            "RECORD-001",
            HusbandryEvidenceRegistry.RecordCategory.Feeding,
            replacementHash
        );
    }

    function testSameRecordIdCanBeUsedInDifferentCategories() public {
        bytes32 growthHash = sha256(bytes("growth record"));
        bytes32 feedingHash = sha256(bytes("feeding record"));

        VM.prank(BREEDER);
        evidenceRegistry.addRecordEvidence(
            "SNAKE001",
            "RECORD-001",
            HusbandryEvidenceRegistry.RecordCategory.Growth,
            growthHash
        );

        VM.prank(BREEDER);
        evidenceRegistry.addRecordEvidence(
            "SNAKE001",
            "RECORD-001",
            HusbandryEvidenceRegistry.RecordCategory.Feeding,
            feedingHash
        );

        require(
            evidenceRegistry.getSnakeRecordCount("SNAKE001") == 2,
            "Different categories must have distinct record keys"
        );
    }

    function testUnknownSnakeCannotReceiveRecordEvidence() public {
        bytes32 recordHash = sha256(bytes("record"));

        VM.expectRevert(SnakeRegistry.SnakeNotFound.selector);
        VM.prank(BREEDER);
        evidenceRegistry.addRecordEvidence(
            "SNAKE999",
            "RECORD-UNKNOWN-001",
            HusbandryEvidenceRegistry.RecordCategory.Health,
            recordHash
        );
    }

    function testHistoryLookupReturnsRecordIdsInAdditionOrder() public {
        bytes32 growthHash = sha256(bytes("growth"));
        bytes32 feedingHash = sha256(bytes("feeding"));

        VM.prank(BREEDER);
        evidenceRegistry.addRecordEvidence(
            "SNAKE001",
            "RECORD-001",
            HusbandryEvidenceRegistry.RecordCategory.Growth,
            growthHash
        );

        VM.prank(BREEDER);
        evidenceRegistry.addRecordEvidence(
            "SNAKE001",
            "RECORD-002",
            HusbandryEvidenceRegistry.RecordCategory.Feeding,
            feedingHash
        );

        HusbandryEvidenceRegistry.RecordReference memory firstRecord =
            evidenceRegistry.getSnakeRecordAt("SNAKE001", 0);
        HusbandryEvidenceRegistry.RecordReference memory secondRecord =
            evidenceRegistry.getSnakeRecordAt("SNAKE001", 1);

        require(
            keccak256(bytes(firstRecord.recordId)) ==
                keccak256(bytes("RECORD-001")),
            "First record ID must be returned at index zero"
        );
        require(
            firstRecord.category ==
                HusbandryEvidenceRegistry.RecordCategory.Growth,
            "First record category must be returned"
        );
        require(
            keccak256(bytes(secondRecord.recordId)) ==
                keccak256(bytes("RECORD-002")),
            "Second record ID must be returned at index one"
        );
        require(
            secondRecord.category ==
                HusbandryEvidenceRegistry.RecordCategory.Feeding,
            "Second record category must be returned"
        );
    }
}
