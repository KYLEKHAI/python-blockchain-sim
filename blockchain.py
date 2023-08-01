'''Import hashlib module for python cryptography functions'''
import hashlib

'''Creating coin block class KhaiCoin'''
class KhaiCoinBlock:

    def __init__(self, prev_block_hash, transaction_list):
        self.prev_block_hash = prev_block_hash
        self.transaction_list = transaction_list

        '''Constructing data string'''
        self.block_data = "->".join(transaction_list) + "->" + prev_block_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()

'''Transactions in blockchain'''
t1 = "Kyle transfered 53 KC to John"
t2 = "Jimmy transfered 21 KC to Alan"
t3 = "Jake transfered 12 KC to Alyssa"
t4 = "Tommy transfered 99 KC to Drake"

'''Creating first block serving as genesis block'''
genesis_block = KhaiCoinBlock(("Initial_Data_String"), [t1,t2])

'''Printing block and hash data pertaining to genesis block'''
print()
print(genesis_block.block_data)
print("Block Hash: "+ genesis_block.block_hash)

second_block = KhaiCoinBlock(genesis_block.block_hash, [t3,t4])

print()
print(second_block.block_data)
print("Block Hash: "+ second_block.block_hash)

'''Note: Changing a value (amount of KC sent in transaction), will cause the entire hashes of the blockchain (future blocks)'''