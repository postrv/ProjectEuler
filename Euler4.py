""" Largest palindrome product
Problem 4
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is
 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers. """

a = 999
ans = 0


def is_palindrome(n):
    if str(n)[::] == str(n)[::-1]:
        return True


while a >= 100:
    b = 999
    while b >= a:
        if a * b <= ans:
            break
        if is_palindrome(a * b):
            ans = a * b
            #print(a, b) optional debug line to check that a and b are correctly iterated
        b -= 1
    a -= 1
print(ans)
