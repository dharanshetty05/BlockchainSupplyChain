import hashlib
import time
import json

class Blockchain:
    def __init__(self):
        # Initialize the blockchain with the genesis block
        self.chain = []
        self.create_block(proof=100, previous_hash='1')  # Genesis block

    def create_block(self, proof, previous_hash):
        # Create a new block and add it to the chain
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time.time(),
            'proof': proof,
            'previous_hash': previous_hash,
            'product_data': {},  # Stores product stage information
        }
        self.chain.append(block)
        return block

    def get_previous_block(self):
        # Return the last block in the chain
        return self.chain[-1]

    def hash(self, block):
        # Generate the SHA-256 hash of a block
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def proof_of_work(self, previous_proof):
        # Implement the Proof-of-Work algorithm
        new_proof = 1
        check_proof = False
        while not check_proof:
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] == '0000':  # Difficulty level: First 4 chars are zero
                check_proof = True
            else:
                new_proof += 1
        return new_proof

    def is_valid(self):
        # Check the validity of the blockchain
        for index in range(1, len(self.chain)):
            current_block = self.chain[index]
            previous_block = self.chain[index - 1]

            # Check if the hash of the previous block matches
            if current_block['previous_hash'] != self.hash(previous_block):
                return False

            # Check if the proof of work is valid
            proof = current_block['proof']
            previous_proof = previous_block['proof']
            hash_operation = hashlib.sha256(str(proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] != '0000':
                return False
        return True

    def add_product_stage(self, product_id, stage, block_index=None):
        # Add a product stage to the specified block
        if block_index is None:
            block_index = len(self.chain) - 1  # Default to the last block
        if product_id not in self.chain[block_index]['product_data']:
            self.chain[block_index]['product_data'][product_id] = []
        self.chain[block_index]['product_data'][product_id].append({
            'stage': stage,
            'timestamp': time.time()
        })

def visualize_blockchain(blockchain):
    from tabulate import tabulate  # Tabulate helps create neat tables
    data = []
    
    for block in blockchain.chain:
        product_data = block['product_data']
        for product_id, stages in product_data.items():
            for stage_info in stages:
                data.append([
                    block['index'],
                    time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(block['timestamp'])),
                    product_id,
                    stage_info['stage'],
                    time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(stage_info['timestamp'])),
                    block['proof'],
                    block['previous_hash'][:10] + "..."
                ])
    
    headers = ["Block Index", "Block Timestamp", "Product ID", "Stage", "Stage Timestamp", "Proof", "Previous Hash"]
    print(tabulate(data, headers=headers, tablefmt="grid"))



# Main function to simulate the supply chain
def simulate_supply_chain():
    # Initialize the blockchain
    blockchain = Blockchain()

    # Stage 1: Manufacturing
    blockchain.add_product_stage(product_id="P12345", stage="Manufacturing")
    previous_block = blockchain.get_previous_block()
    proof = blockchain.proof_of_work(previous_block['proof'])
    previous_hash = blockchain.hash(previous_block)
    blockchain.create_block(proof, previous_hash)

    # Stage 2: Shipping
    blockchain.add_product_stage(product_id="P12345", stage="Shipping")
    previous_block = blockchain.get_previous_block()
    proof = blockchain.proof_of_work(previous_block['proof'])
    previous_hash = blockchain.hash(previous_block)
    blockchain.create_block(proof, previous_hash)

    # Stage 3: Quality Check
    blockchain.add_product_stage(product_id="P12345", stage="Quality Check")
    previous_block = blockchain.get_previous_block()
    proof = blockchain.proof_of_work(previous_block['proof'])
    previous_hash = blockchain.hash(previous_block)
    blockchain.create_block(proof, previous_hash)

    # Stage 4: Delivered
    blockchain.add_product_stage(product_id="P12345", stage="Delivered")
    previous_block = blockchain.get_previous_block()
    proof = blockchain.proof_of_work(previous_block['proof'])
    previous_hash = blockchain.hash(previous_block)
    blockchain.create_block(proof, previous_hash)

    # Validate the blockchain
    print(f"Blockchain valid: {blockchain.is_valid()}")

    # Print the blockchain for inspection
    for block in blockchain.chain:
        print(json.dumps(block, indent=4, default=str))

    # Visualize the blockchain
    print("\nBlockchain Visualization:")
    visualize_blockchain(blockchain)



# Run the simulation
if __name__ == "__main__":
    simulate_supply_chain()
