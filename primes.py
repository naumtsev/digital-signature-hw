import random
from pows import fast_pow_by_mod, fast_pow


def n_bits_random_prime(n_bits: int) -> int:
    while True:
        prime_candidate = get_candidate(n_bits)
        if is_miller_rabin_test_passed(prime_candidate) and is_prime(prime_candidate):
            return prime_candidate


def is_prime(n: int) -> bool:
    c = int(n ** 0.5 + 0.5)
    for i in range(2, c):
        if n % i == 0:
            return False
    return True


small_primes_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
                     101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197,
                     199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313,
                     317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439,
                     443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571,
                     577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691,
                     701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829,
                     839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977,
                     983, 991, 997]


def n_bits_random_number(n: int) -> int:
    return random.randrange(2 ** (n - 1) + 1, 2 ** n - 1)


def get_candidate(n_bits) -> int:
    while True:
        candidate = n_bits_random_number(n_bits)
        for d in small_primes_list:
            if candidate % d == 0 and d ** 2 <= candidate:
                break
        else:
            return candidate


def is_miller_rabin_test_passed(prime_candidate):
    max_divs_by_two = 0
    remainder = prime_candidate - 1
    while remainder % 2 == 0:
        remainder >>= 1
        max_divs_by_two += 1

    def test_miller(near_prime: int) -> bool:
        if fast_pow_by_mod(near_prime, remainder, prime_candidate) == 1:
            return False

        for i in range(max_divs_by_two):
            if fast_pow_by_mod(near_prime, fast_pow(2, i) * remainder, prime_candidate) == prime_candidate - 1:
                return False
        return True

    tries = 20
    for i in range(tries):
        round_tester = random.randrange(2, prime_candidate)
        if test_miller(round_tester):
            return False
    return True
