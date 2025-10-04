import multiprocessing
import time
import random
from datetime import datetime

def worker(name):
    # Sleep for a random time between 0 and 1 second
    wait_time = random.random()
    time.sleep(wait_time)
    # Print worker name and current time
    print(f"Process {name} finished at {datetime.now().strftime('%H:%M:%S.%f')} after {wait_time:.2f} seconds")

if __name__ == "__main__":
    # Create three processes
    processes = []
    for i in range(3):
        p = multiprocessing.Process(target=worker, args=(i,))
        processes.append(p)
        p.start()

    # Wait for all processes to complete
    for p in processes:
        p.join()