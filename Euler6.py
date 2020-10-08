""" Sum square difference
Problem 6
The sum of the squares of the first ten natural numbers is,

The square of the sum of the first ten natural numbers is,

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum. """

import time

t0 = time.time()
num = 101  # adjusted up to avoid off-by-one error but need to find a more elegant way of handling this in ranges
s_sum = 0
sum_squares = 0

for x in range(num):
    sum_squares += x ** 2
    s_sum += x
print(s_sum ** 2 - sum_squares)
t1 = time.time()
print(t1 - t0)
