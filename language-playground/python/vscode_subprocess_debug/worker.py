import time

def worker():
    """worker function"""
    while True:
        temp = 1
        time.sleep(1)

if __name__ == "__main__":
    worker()