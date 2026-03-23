import secrets


def random_key(n):
    return secrets.token_bytes(n)


def otp_encrypt(message_bytes, key):
    if len(message_bytes) != len(key):
        raise ValueError("message and key must have same length")
    out = bytearray()
    for i in range(len(message_bytes)):
        out.append(message_bytes[i] ^ key[i])
    return bytes(out)


def otp_decrypt(cipher_bytes, key):
    return otp_encrypt(cipher_bytes, key)


msg = b"attack"
key = random_key(len(msg))
c = otp_encrypt(msg, key)
p = otp_decrypt(c, key)
print(p)
