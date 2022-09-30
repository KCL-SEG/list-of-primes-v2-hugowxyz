"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""


def isPrime(n):
    for i in range(2, int(n**(1/2)) + 1):
        if n % i == 0:
            return False

    return True


def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError()

    list = []
    counter = 2
    while len(list) < number_of_primes:
        if isPrime(counter):
            list.append(counter)
        counter += 1

    return list
