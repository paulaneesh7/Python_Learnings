

# Exponential Backoff

import time

def exponential_backoff(max_retries=5, initial_wait=1):
    wait_time = initial_wait
    for retry in range(1, max_retries + 1):
        print(f"Attempt {retry}: Waiting for {wait_time} seconds before retrying...")
        time.sleep(wait_time)
        wait_time *= 2  # Double the wait time for the next retry

    print("Max retries reached. Exiting...")

# Call the function
exponential_backoff()