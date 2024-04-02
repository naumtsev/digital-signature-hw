def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = extended_gcd(b % a, a)
        return g, x - (b // a) * y, y


def gcd(a, b):
    while a != 0:
        a, b = b % a, a
    return b


def mod_inverse(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m


def fast_pow_by_mod(a: int, n: int, mod: int) -> int:
    if n == 0:
        return 1
    elif n == 1:
        return a % mod
    else:
        c = fast_pow_by_mod(a, n // 2, mod)
        return (c * c * (a if n & 1 else 1)) % mod


def fast_pow(a: int, n: int) -> int:
    if n == 0:
        return 1
    elif n == 1:
        return a
    else:
        c = fast_pow(a, n // 2)
        return c * c * (a if n & 1 else 1)


