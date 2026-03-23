import random


p = 23
g = 5


def private_key():
    return random.randint(2, p - 2)


def public_key(a):
    return pow(g, a, p)


def shared_key(other_public, my_private):
    return pow(other_public, my_private, p)


a = private_key()
b = private_key()
A = public_key(a)
B = public_key(b)
s1 = shared_key(B, a)
s2 = shared_key(A, b)
print(s1 == s2)
