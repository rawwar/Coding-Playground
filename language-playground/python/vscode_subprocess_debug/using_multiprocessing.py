# simple multiprocess code that spawns a subprocess to run a for loop that iterates till 100 and stops

import multiprocessing
import time


def worker():
    """worker function"""
    while True:
        temp = 1
        time.sleep(1)        
    return

if __name__ == '__main__':
    jobs = []
    for i in range(1):
        p = multiprocessing.Process(target=worker)
        jobs.append(p)
        p.start()
    p.join()