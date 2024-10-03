import hashlib
import time

def calculate_hash(data):
    """Calculate the SHA-256 hash of the input data."""
    return hashlib.sha256(data.encode('utf-8')).hexdigest()

def measure_hashrate(duration=1):
    """Measure how many hashes can be performed in a given duration (in seconds)."""
    start_time = time.time()
    count = 0
    data = "This is some test data for hashing"
    
    while time.time() - start_time < duration:
        # Calculate a hash
        calculate_hash(data + str(count))
        count += 1

    # Hashes per second (H/s)
    hashrate = count / duration
    return hashrate

# Step 1: Measure your PC's hashrate
hashrate = measure_hashrate(1)
print(f"Your PC's hashrate: {hashrate} hashes per second (H/s)")

# Step 2: Compare to the Bitcoin network hashrate (approx 450 EH/s = 450 * 10^18 H/s)
network_hashrate = 450 * 10**18  # 450 exahashes per second

# Step 3: Estimate time to find a block
# Bitcoin finds a block approximately every 600 seconds
expected_block_time = 600  # in seconds

# Time to find a block with your PC
time_to_find_block = (expected_block_time * network_hashrate) / hashrate

# Convert time to years for better understanding
time_in_years = time_to_find_block / (60 * 60 * 24 * 365)

print(f"Estimated time to find a block with your PC: {time_in_years} years")
