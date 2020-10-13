""" 10001st prime
Problem 7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number? """

#  prime number definer (true for all in range upper limit(n)
#  prime number eliminator using Sieve of Eratosthenes
#  counter

import time
from math import log, ceil

t0 = time.time()
num = 100001
prime_count = 0


def upper_bound(n):  #  returns the theoretical upper bound for the nth prime given n
    if n < 6:
        return 100
    return ceil(n * (log(n) + log(log(n))))


def get_primes(n):  #  returns primes for a given range n
    primes = [True for i in range(n+1)]  #  creates an initial masked boolean array set to True
    primes[0] = False
    primes[1] = False
    actual_primes = []
    p = 2
    while p * p < n:
        if primes[p]:
            for x in range(p * 2, n + 1, p):
                primes[x] = False  #  updates the masked array value to False for any product of a prime
        p += 1
    for p in range(2, n+1):
        if primes[p]:
            actual_primes.append(p)  #  creates an array containing the True primes
    return actual_primes


def nth_prime(n):
    primes_to_n = list(get_primes(upper_bound(n)))
    return primes_to_n[n-1]


print(nth_prime(10001))


t1 = time.time()
print(t1-t0)