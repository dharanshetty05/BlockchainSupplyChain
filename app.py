from flask import Flask, render_template, request, jsonify
import time
import hashlib

# Blockchain code (same as before, adapted for Flask)
class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_block(proof=100, previous_hash='1', product_data={})

    def create_block(self, proof, previous_hash, product_data):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time.time(),
            'proof': proof,
            'previous_hash': previous_hash,
            'product_data': product_data
        }
        self.chain.append(block)
        return block

    def get_previous_block(self):
        return self.chain[-1]

    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False
        while not check_proof:
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] == '0000':
                check_proof = True
            else:
                new_proof += 1
        return new_proof

    def hash(self, block):
        encoded_block = str(block).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    def is_chain_valid(self):
        previous_block = self.chain[0]
        block_index = 1

        while block_index < len(self.chain):
            block = self.chain[block_index]
            if block['previous_hash'] != self.hash(previous_block):
                return False

            proof = block['proof']
            previous_proof = previous_block['proof']
            hash_operation = hashlib.sha256(str(proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] != '0000':
                return False

            previous_block = block
            block_index += 1
        return True


# Flask application
app = Flask(__name__)
blockchain = Blockchain()

@app.route('/')
def index():
    return render_template('index.html', blockchain=blockchain.chain)

@app.route('/add_product', methods=['POST'])
def add_product():
    product_id = request.form['product_id']
    stage = request.form['stage']
    
    # Add product data to blockchain
    previous_block = blockchain.get_previous_block()
    proof = blockchain.proof_of_work(previous_block['proof'])
    previous_hash = blockchain.hash(previous_block)

    product_data = previous_block['product_data']
    if product_id not in product_data:
        product_data[product_id] = []
    product_data[product_id].append({
        'stage': stage,
        'timestamp': time.time()
    })
    
    blockchain.create_block(proof, previous_hash, product_data)
    return jsonify({'message': 'Product stage added successfully!'}), 200

@app.route('/validate', methods=['GET'])
def validate():
    is_valid = blockchain.is_chain_valid()
    return jsonify({'valid': is_valid}), 200

if __name__ == '__main__':
    app.run(debug=True)
