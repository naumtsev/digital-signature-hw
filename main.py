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


def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = extended_gcd(b % a, a)
        return g, x - (b // a) * y, y


def mod_inverse(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m


def generate_keys() -> (PublicKey, PrivateKey):
    p = random_prime()
    q = random_prime()

    while q == p:
        q = random_prime()

    n = p * q
    m = (p - 1) * (q - 1)
    d = random_coprime_number(m)
    e = mod_inverse(d, m)
    return PublicKey(e, n), PrivateKey(d, n)


def fast_pow(a: int, n: int, mod: int) -> int:
    if n == 0:
        return 1
    elif n == 1:
        return a % mod
    else:
        c = fast_pow(a, n // 2, mod)
        return (c * c * (a if n & 1 else 1)) % mod


def encrypt(message: int, public_key: PublicKey) -> int:
    return fast_pow(message, public_key.e, public_key.n)


def decrypt(ciphertext: int, private_key: PrivateKey) -> int:
    return fast_pow(ciphertext, private_key.d, private_key.n)