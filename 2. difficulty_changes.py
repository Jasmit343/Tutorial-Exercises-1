import hashlib
import time

def calculate_hash(data):
    """Calculate the SHA-256 hash of the input data."""
    return hashlib.sha256(data.encode('utf-8')).hexdigest()

def proof_of_work(data, target):
    """Perform proof-of-work by finding a nonce such that hash(data + nonce) < target."""
    nonce = 0
    block_found = False
    start_time = time.time()
    
    while not block_found:
        block_data = f"{data}{nonce}"
        block_hash = calculate_hash(block_data)
        
        if block_hash < target:
            end_time = time.time()
            time_taken = end_time - start_time
            return nonce, block_hash, time_taken
        else:
            nonce += 1

def adjust_difficulty(current_target, time_taken, expected_time):
    """Adjust difficulty based on the time it took to mine the block."""
    
    if time_taken < expected_time:
        
        current_target = increase_difficulty(current_target)
        print("Increasing difficulty to:", current_target)
    else:
        
        current_target = decrease_difficulty(current_target)
        print("Decreasing difficulty to:", current_target)
    
    return current_target

def increase_difficulty(target):
    """Increase difficulty by adding one leading zero, if possible."""
    
    return '0' + target[:-1]

def decrease_difficulty(target):
    """Decrease difficulty by removing one leading zero, if possible."""
    
    if target.startswith('0000'):
        return target[1:] + 'f'  
    return target

block_data = "This is some block data"
initial_target = "0000fffffffffffffffffffffffffffffffffffffffffffffffffffffffffff"

expected_time = 10  

current_target = initial_target
block_count = 0

while block_count < 5:  
    print(f"\nMining block {block_count + 1} with difficulty target: {current_target}")
    nonce, block_hash, time_taken = proof_of_work(block_data, current_target)
    
    print(f"Block {block_count + 1} found!")
    print(f"Nonce: {nonce}")
    print(f"Hash: {block_hash}")
    print(f"Time taken: {time_taken} seconds")
    
    current_target = adjust_difficulty(current_target, time_taken, expected_time)
    
    block_count += 1
