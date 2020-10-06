""" Largest prime factor
Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ? """

number = 600851475143
factor = 2

while factor * factor < number:
    while number % factor == 0:
        number = number // factor
    factor += 1
print(number)