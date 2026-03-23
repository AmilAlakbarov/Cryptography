import random


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    raise ValueError("no inverse")


def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def random_prime(start=100, end=300):
    while True:
        p = random.randint(start, end)
        if is_prime(p):
            return p


def keygen():
    p = random_prime()
    q = random_prime()
    while q == p:
        q = random_prime()

    n = p * q
    phi = (p - 1) * (q - 1)

    e = 65537
    if gcd(e, phi) != 1:
        e = 3
        while gcd(e, phi) != 1:
            e += 2

    d = mod_inverse(e, phi)
    return (n, e), (n, d)


def encrypt(m, pub):
    n, e = pub
    return pow(m, e, n)


def decrypt(c, prv):
    n, d = prv
    return pow(c, d, n)


pub, prv = keygen()
m = 1234
c = encrypt(m, pub)
p = decrypt(c, prv)
print(m == p)
