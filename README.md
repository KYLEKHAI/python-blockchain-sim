# python-crypto-blockchain-sim

### The following files simulate the functionality of cryptocurrency and blockchain feautures

## blockchain.py

- The code serves as a basic illustration of how blockchain technology maintains the integrity and security of data in distributed networks.
- The code defines a custom class named `KhaiCoinBlock`, representing individual blocks in the blockchain.
- Each block contains a previous block's hash and a list of transactions, represented as strings in the form of "Sender transferred Amount KC to Receiver."
- The data for the block is constructed by concatenating the transaction list and the previous block's hash, and the SHA-256 hash is computed as the block's unique identifier.
- The first block, called the "genesis block," is created with an initial data string and a list of transactions (t1, t2).
- Subsequent blocks are created with the previous block's hash as a reference and a new list of transactions (t3, t4).
- The blockchain ensures data integrity, as changing any transaction or block content will alter the subsequent block hashes.
- The code uses the Python `hashlib` module for cryptographic hashing functions, and a class called `KhaiCoinBlock` represents each block in the blockchain.

## candlestick-charts.py

- This Python code visualizes the price movements of a chosen crypto or stock.
- It fetches financial data from Yahoo Finance for the specified asset and date range.
- The data is displayed in a customizable candlestick chart.
- Users can analyze open, high, low, and close (OHLC) prices, along with volume data.
- The chart helps traders identify trends and make informed financial decisions.
- The code utilizes Python modules and libraries, including `matplotlib.pyplot`, `yfinance`, `mplfinance`, and `datetime`.
- `yfinance` allows easy access to financial data from Yahoo Finance.
- `mplfinance` is a specialized library for creating financial and candlestick charts.
- The script prompts users to input the asset symbol and start date, validates the input, and fetches financial data accordingly.
- Custom market colors are used for the candlestick chart, providing visual cues for upward and downward price movements.
- The chart is plotted using the chosen chart type ("candle," "line," etc.), and the `warn_too_much_data` parameter is set to suppress data size warnings.
- Traders can customize the chart and analyze asset price trends effectively.

## bitcoin-miner.py

- This Python code simulates a basic bitcoin mining process to find a specific number (nonce) that results in a hash with a specified number of leading zeroes.
- The user can input the mining difficulty level, represented by the number of leading zeroes to find in the hash.
- The `mine` function attempts to find the required nonce by iterating through a range of nonce values (from 0 to `NONCE_LIMIT`).
- For each nonce, the function constructs a base text by concatenating the block number, transactions, previous hash, and the current nonce value.
- The SHA-256 hash of the base text is calculated and checked to see if it starts with the required number of leading zeroes.
- If a valid hash is found, the function returns the hash with the corresponding nonce value.
- If no valid hash is found within the nonce limit, the function returns -1 to indicate failure.
- The code then sets up example data with a block number, transactions, and previous hash to demonstrate the mining process.
- The mining process is executed using the `mine` function, and the resulting hash with the corresponding nonce is printed.
