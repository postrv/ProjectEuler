""" Largest palindrome product
Problem 4
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is
 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers. """


import time

a = 999
ans = 0
t0 = time.time()


def is_palindrome(n):
    if str(n)[::] == str(n)[::-1]:
        return True


for a in range(1000, 100, -1):
    b = 999
    for b in range(1000, a, -1):
        if a * b <= ans:
            break
        if is_palindrome(a * b):
            ans = a * b
            #print(a, b) optional debug line to check that a and b are correctly iterated
        b -= 1
    a -= 1
print(ans)
t1 = time.time()
print(t1-t0)