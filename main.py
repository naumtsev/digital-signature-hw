# RSA Algorithm

import sympy
import random

MIN_PRIME_NUMBER = 10000
MAX_PRIME_NUMBER = 1000000


class PrivateKey:
    def __init__(self, d: int, n: int):
        self.d = d
        self.n = n

    def __repr__(self):
        return f'd: {self.d}, n: {self.n}'


class PublicKey:
    def __init__(self, e: int, n: int):
        self.e = e
        self.n = n

    def __repr__(self):
        return f'd: {self.e}, n: {self.n}'


def random_prime():
    return sympy.randprime(MIN_PRIME_NUMBER, MAX_PRIME_NUMBER)


def random_coprime_number(n: int) -> int:  # gcd(result, n) = 1
    x = random.randint(2, n)
    while sympy.gcd(x, n) != 1:
        x = random.randint(2, n)
    return x


def generate_keys() -> (PublicKey, PrivateKey):
    p = random_prime()
    q = random_prime()

    while q == p:
        q = random_prime()

    n = p * q
    m = (p - 1) * (q - 1)
    d = random_coprime_number(m)
    e = sympy.mod_inverse(d, m)

    return PublicKey(e, n), PrivateKey(d, n)


def encrypt(message: int, public_key: PublicKey):
    return pow(message, public_key.e, public_key.n)


def decrypt(ciphertext: int, private_key: PrivateKey):
    return pow(ciphertext, private_key.d, private_key.n)
