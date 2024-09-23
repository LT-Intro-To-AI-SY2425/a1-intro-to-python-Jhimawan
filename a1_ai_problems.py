# Complete your individualized AI problems here

"""def fizbuzz(input_num):
    if(input_num%3==0):
        if(input_num%5==0):
            return 'FizzBuzz'
        return 'Fizz'
    elif(input_num%5==0):
        return 'Buzz'
    else:
        return input_num

assert fizbuzz(1) == 1, "fizzbuzz 1 test"
assert fizbuzz(3) == "Fizz", "fizzbuzz 3 test"
assert fizbuzz(4) == 4, "fizzbuzz 4 test"
assert fizbuzz(5) == "Buzz", "fizzbuzz 5 test"
assert fizbuzz(6) == "Fizz", "fizzbuzz 6 test"
assert fizbuzz(15) == "FizzBuzz", "fizzbuzz 15 test"
"""""

def fibonacci(n):

    a, b = 0, 1

    while a < n:
        a, b = b, b + a

    return b

def factorial(n):
    x = 1
    for i in range(1, n + 1, n):
        x *= i
    return x


def count_vowels(n):
    x = 0
    i = 0
    n = n.lower()
    for letter in n:
        if ord(letter) == a:

    return x