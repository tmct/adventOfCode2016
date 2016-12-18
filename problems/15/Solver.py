from operator import mul
from functools import reduce


def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


class Solver:
    def solve(self, primes, remainders):
        prime_product = reduce(mul, primes, 1)
        inverses = [modinv(prime_product // prime, prime) for prime in primes]
        return sum(remainders[i] * inverses[i] * (prime_product // primes[i]) for i in
                          range(len(primes))) % prime_product
