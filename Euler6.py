""" Sum square difference
Problem 6
The sum of the squares of the first ten natural numbers is,

The square of the sum of the first ten natural numbers is,

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum. """

num = 101#  adjusted up to avoid off-by-one error but need to find a more elegant way of handling this in ranges

def sum_squares(x):
    ans1 = 0
    for i in range(x):
        ans1 += i**2
    return ans1



def square_sums(y):
    ans2 = 0
    for n in range(y):
        ans2 += n
    return (ans2 ** 2)

print(sum_squares(num))
print(square_sums(num))
print(abs(sum_squares(num) - square_sums(num)))
