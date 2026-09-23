import hashlib
import json
from datetime import datetime, timezone


class Block:
    def __init__(self, index, timestamp, transaction_data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.transaction_data = transaction_data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()


    def calculate_hash(self):
        block_contents = {
            "index": self.index,
            "timestamp": self.timestamp,
            "transaction_data": self.transaction_data,
            "previous_hash": self.previous_hash,
        }
        encoded_contents = json.dumps(
            block_contents, sort_keys=True, separators=(",", ":")
        ).encode("utf-8")
        return hashlib.sha256(encoded_contents).hexdigest()


    def __str__(self):
        return (
            f"Block {self.index + 1}\n"
            f"Index: {self.index}\n"
            f"Timestamp: {self.timestamp}\n"
            f"Transaction: {self.transaction_data}\n"
            f"Previous hash: {self.previous_hash}\n"
            f"Current hash:  {self.hash}"
        )


class Blockchain:


    def __init__(self):
        self.chain = [self.create_genesis_block()]


    @staticmethod
    def current_timestamp():
        return datetime.now(timezone.utc).isoformat()


    def create_genesis_block(self):
        return Block(
            index=0,
            timestamp=self.current_timestamp(),
            transaction_data="Genesis Block",
            previous_hash="0",
        )


    def add_block(self, transaction_data):
        previous_block = self.chain[-1]
        new_block = Block(
            index=len(self.chain),
            timestamp=self.current_timestamp(),
            transaction_data=transaction_data,
            previous_hash=previous_block.hash,
        )
        self.chain.append(new_block)


    def validate_chain(self):
        for position, current_block in enumerate(self.chain):
            recalculated_hash = current_block.calculate_hash()

            if current_block.hash != recalculated_hash:
                return False, {
                    "block_number": position + 1,
                    "index": current_block.index,
                    "reason": "The stored hash does not match the block contents.",
                    "stored_hash": current_block.hash,
                    "recalculated_hash": recalculated_hash,
                }

            if position == 0:
                if current_block.previous_hash != "0":
                    return False, {
                        "block_number": 1,
                        "index": 0,
                        "reason": "The genesis block has an invalid previous hash.",
                    }
                continue

            previous_block = self.chain[position - 1]
            if current_block.previous_hash != previous_block.hash:
                return False, {
                    "block_number": position + 1,
                    "index": current_block.index,
                    "reason": "The link to the previous block is invalid.",
                    "stored_previous_hash": current_block.previous_hash,
                    "expected_previous_hash": previous_block.hash,
                }

        return True, {"message": "All blocks and hash links are valid."}


    def print_chain(self):
        for block in self.chain:
            print(block)
            print("-" * 80)


def print_validation_result(blockchain):
    is_valid, details = blockchain.validate_chain()
    print(f"Blockchain valid: {is_valid}")

    if is_valid:
        print(details["message"])
    else:
        print(f"First invalid block: Block {details['block_number']}")
        print(f"Block index: {details['index']}")
        print(f"Reason: {details['reason']}")
        for key, value in details.items():
            if key not in {"block_number", "index", "reason"}:
                print(f"{key.replace('_', ' ').title()}: {value}")


def main():
    blockchain = Blockchain()

    transactions = [
        "Rose pays Bob 2.6 BTC",
        "Bob pays Charlie 0.3 BTC",
        "Charlie pays Diana 1.2 BTC",
        "Diana pays Ethan 0.5 BTC",
        "Ethan pays Max 3.3 BTC",
        "Max pays George 0.9 BTC",
        "George pays Hannah 1.8 BTC",
        "Hannah pays Isaac 0.2 BTC",
        "Isaac pays Julia 2.0 BTC",
    ]

    for transaction in transactions:
        blockchain.add_block(transaction)

    print("BLOCKCHAIN BEFORE MODIFICATION:")
    print("=" * 80)
    blockchain.print_chain()
    print_validation_result(blockchain)

    # The genesis block counts as block 1 so list position 4 is the 5th block
    blockchain.chain[4].transaction_data = "Unauthorized transfer of 1 BTC"

    print("\nBLOCKCHAIN AFTER MODIFYING THE 5TH BLOCK:")
    print("=" * 80)
    blockchain.print_chain()
    print_validation_result(blockchain)


if __name__ == "__main__":
    main()



