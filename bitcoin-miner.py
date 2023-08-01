'''Building a bitcoin miner that finds a specific number (nonce) that produces leading zeroes (resulting in a hash --> bitcoin)'''

import hashlib

'''Initializing variables (randomizer limit & condition)'''
NONCE_LIMIT = 1000000000

'''Mining difficulty'''
zeroes = 4 

''''''
def mine(block_num, transactions, prev_hash): 
    
    '''Up until this limit, build a new base text'''
    for nonce in range(NONCE_LIMIT):

        '''Concatenating block number, transactions, previous hash, and nonce'''
        base_text = str(block_num) + transactions + prev_hash + str(nonce)
        
        '''Saves the hash data and calculate the SHA-256 hash of the base text'''
        hash_attempt = hashlib.sha256(base_text.encode().hexdigest())

        '''Loop that checks if the hash starts with the required number of leading zeroes'''
        if hash_attempt.startswith("0" * zeroes):
            print(f"Found hash with nonce: {nonce}")
            return hash_attempt
        
        # If the hash does not meet the required condition, try the next nonce value

        # If no valid hash is found within the nonce limit, return -1 to indicate failure
        return -1
    
    