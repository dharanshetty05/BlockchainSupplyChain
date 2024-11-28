# Blockchain-Based Supply Chain Management System

## Overview
This project implements a Blockchain-Based Supply Chain Management System using Python. The system securely tracks products across the supply chain using cryptographic hashing (SHA-256) and immutable records. It ensures transparency and verifies the authenticity of products at each stage of the supply chain. The project also integrates product stage tracking and tampering detection, with real-time updates to maintain supply chain integrity.

## Key Features
- **Blockchain**: Ensures the immutability and transparency of product data throughout the supply chain.
- **SHA-256 Cryptographic Hashing**: Provides secure and verifiable data storage for each product stage.
- **Real-Time Product Stage Tracking**: Tracks the product's journey from Manufacturing to Delivery.
- **Tampering Detection**: Ensures the integrity of product data at each stage.
- **UI (Optional)**: A simple user interface to interact with the blockchain and visualize the product's movement through the supply chain.

## Technologies Used
- **Python**: The core programming language used for building the blockchain and the system logic.
- **Flask**: Used for building the web interface (if applicable).
- **SQLite (Optional)**: A lightweight database for storing transaction details.
- **Cryptography**: SHA-256 hashing algorithm used for creating secure product stages.
- **Git**: Version control for managing and tracking changes to the project.

## Project Structure
```
BlockchainSupplyChain
├── blockchain.py  # Core Blockchain logic and cryptographic functions
├── app.py         # Flask app for UI (if applicable)
├── README.md      # Project documentation (this file)
└── requirements.txt # Python dependencies
```

## Setup and Installation

### Prerequisites
- Python 3.x installed on your system.
- Git for version control.
- Optionally, Flask and cryptography libraries.

### Steps to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/dharanshetty05/BlockchainSupplyChain.git
   ```
2. Navigate into the project directory:
   ```bash
   cd BlockchainSupplyChain
   ```
3. Install the necessary dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the Python script to start the blockchain and test the supply chain system:
   ```bash
   python blockchain.py
   ```
5. (Optional) If you want to run the UI:
   ```bash
   python app.py
   ```
6. Open your browser and go to:
   ```
   http://127.0.0.1:5000/
   ```

## Requirements File
The `requirements.txt` file includes the necessary libraries for the project:
```
flask==2.0.1
cryptography==3.4.7
```
Install the dependencies with:
```bash
pip install -r requirements.txt
```

## Example Usage
Once the system is running, you can interact with it via the UI (if implemented) or via the console (if it's a command-line-based implementation). Below is a sample of how the blockchain works when tracking a product through different stages:

1. **Manufacturing:** Product is created and logged with a timestamp.
2. **Shipping:** Product is shipped and tracked.
3. **Quality Check:** Product undergoes quality verification.
4. **Delivered:** Product is delivered and confirmed.

The blockchain ensures that no information can be altered without detection, guaranteeing the integrity of the product's journey.

## Blockchain Validation
The blockchain is validated using the following criteria:

- Each block contains a cryptographic hash of the previous block, ensuring the immutability of the chain.
- The product stage data is encrypted and stored securely in the blockchain to avoid tampering.

Validate the blockchain by running:
```bash
python blockchain.py
```

## Contributing
Feel free to fork the repository, make changes, and submit pull requests! If you find any bugs or have suggestions for improvements, please open an issue.

## License
This project is open source and available under the MIT License.
