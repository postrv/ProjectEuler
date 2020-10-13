""" Sum square difference
Problem 6
The sum of the squares of the first ten natural numbers is,

The square of the sum of the first ten natural numbers is,

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum. """

import time

t0 = time.time()
num = 100

def difference(n):
    sum_square = n * (n+1) // 2
    square_sum = n * (n+1) * (2 * n + 1) // 6
    return sum_square * sum_square - square_sum


print(difference(100))