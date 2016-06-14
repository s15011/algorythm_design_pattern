#!/usr/bin/env python3
import time

def isPrime(n):
    isPrime = True
    for i in range(2, (n - 1)):
        if(n % i == 0):
            isPrime = False
            return False

    if(isPrime == True):
        return True

if __name__ == '__main__':

    start = time.time()
    for i in range(1000):
        isPrime(i)
    end = time.time()
    print("経過時間:", (end - start))
