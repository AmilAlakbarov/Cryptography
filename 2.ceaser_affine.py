def caesar_encrypt(text, shift):
    out = ""
    for ch in text:
        if ch.isalpha():
            if ch.isupper():
                base = ord("A")
            else:
                base = ord("a")
            out += chr((ord(ch) - base + shift) % 26 + base)
        else:
            out += ch
    return out


def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def mod_inverse(a, m):
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    raise ValueError("No inverse")


def affine_encrypt(text, a, b):
    if gcd(a, 26) != 1:
        raise ValueError("a must be coprime with 26")

    out = ""
    for ch in text:
        if ch.isalpha():
            if ch.isupper():
                base = ord("A")
            else:
                base = ord("a")
            x = ord(ch) - base
            y = (a * x + b) % 26
            out += chr(y + base)
        else:
            out += ch
    return out


def affine_decrypt(text, a, b):
    a_inv = mod_inverse(a, 26)
    out = ""
    for ch in text:
        if ch.isalpha():
            if ch.isupper():
                base = ord("A")
            else:
                base = ord("a")
            y = ord(ch) - base
            x = (a_inv * (y - b)) % 26
            out += chr(x + base)
        else:
            out += ch
    return out


c = caesar_encrypt("hello", 3)
print(c, caesar_decrypt(c, 3))
a = affine_encrypt("hello", 5, 8)
print(a, affine_decrypt(a, 5, 8))
