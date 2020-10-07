""" Smallest multiple
Problem 5
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20? """

#  code to genuinely laugh at
#  find the prime factors
#  find the composites that eliminate the need to test their prime factors e.g. 15 and 18 eliminate 3
#  make a record of these exponents
#  multiply the terms together

primes = []
not_primes = []
ans = 1

import time
t0 = time.time()
def is_prime(x):
    if x <= 1:
        return False
    if x == 2:
        return True
    else:
        for i in range(2, x, 1):#  could divide x // 2 here but causes 4 to return false
            if (x % i) == 0:
                return False
        else:
            return True


for n in range(1 , 21):
    if is_prime(n):
        primes.append(n)
    else:
        not_primes.append(n)

print(primes)
print(not_primes)
exponent_ct_2 = -1  #  because these numbers already exist in the list of primes we want to subtract 1 when finding exponent
exponent_ct_3 = -1

for a in primes:  #  finding the exponents to generate the composites and complete the list
    for b in primes:
        for c in not_primes:
            if a*b == c:
                if a == 2:
                    exponent_ct_2 += 1
                else:
                    if a == 3:
                        if b % 2 != 0:
                            exponent_ct_3 += 1


exponents = (2**(exponent_ct_2)*3**(exponent_ct_3))
for x in primes:
    ans *= x
print(ans*exponents)
t1 = time.time()
print(t0 - t1)