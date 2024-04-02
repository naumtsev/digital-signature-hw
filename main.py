# RSA Algorithm

import random
from primes import n_bits_random_prime
from pows import mod_inverse, fast_pow_by_mod, gcd

N_BITS = 20


def random_prime():
    return n_bits_random_prime(N_BITS)


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


def random_coprime_number(n: int) -> int:  # gcd(result, n) = 1
    x = random.randint(2, n)
    while gcd(x, n) != 1:
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
    e = mod_inverse(d, m)
    return PublicKey(e, n), PrivateKey(d, n)


def encrypt(message: int, public_key: PublicKey) -> int:
    return fast_pow_by_mod(message, public_key.e, public_key.n)


def decrypt(ciphertext: int, private_key: PrivateKey) -> int:
    return fast_pow_by_mod(ciphertext, private_key.d, private_key.n)
