import hashlib
import time

def calculate_hash(data):
    return hashlib.sha256(data.encode('utf-8')).hexdigest()

def proof_of_work(data, target, time_limit=30):
    nonce = 0
    block_found = False
    start_time = time.time()
    
    while not block_found and (time.time() - start_time) < time_limit:
        block_data = f"{data}{nonce}"
        block_hash = calculate_hash(block_data)
        
        if block_hash < target:
            block_found = True
            end_time = time.time()
            print(f"Block found with nonce {nonce}")
            print(f"Hash: {block_hash}")
            print(f"Time taken: {end_time - start_time} seconds")
            return nonce, block_hash
        else:
            nonce += 1

        if nonce % 100000 == 0:
            print(f"Still mining... Nonce: {nonce}")

    if not block_found:
        print(f"Time limit reached, block not found after {time_limit} seconds.")
    return None

block_data = "This is some block data"

target_low_difficulty = "0000fffffffffffffffffffffffffffffffffffffffffffffffffffffffffff"
target_high_difficulty = "000000fffffffffffffffffffffffffffffffffffffffffffffffffffffffffff"
target_very_high_difficulty = "0000000fffffffffffffffffffffffffffffffffffffffffffffffffffffffffff"

print("Mining with low difficulty:")
proof_of_work(block_data, target_low_difficulty)

print("\nMining with high difficulty:")
proof_of_work(block_data, target_high_difficulty)

print("\nMining with very high difficulty:")
proof_of_work(block_data, target_very_high_difficulty)
