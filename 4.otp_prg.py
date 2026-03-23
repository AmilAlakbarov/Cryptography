import hashlib
import secrets


def prg(seed, length):
    data = b""
    counter = 0
    while len(data) < length:
        block = hashlib.sha256(seed + counter.to_bytes(4, "big")).digest()
        data += block
        counter += 1
    return data[:length]


def otp_prg_encrypt(message_bytes, seed):
    key = prg(seed, len(message_bytes))
    out = bytearray()
    for i in range(len(message_bytes)):
        out.append(message_bytes[i] ^ key[i])
    return bytes(out)


def otp_prg_decrypt(cipher_bytes, seed):
    return otp_prg_encrypt(cipher_bytes, seed)


seed = secrets.token_bytes(16)
msg = b"hello crypto"
c = otp_prg_encrypt(msg, seed)
p = otp_prg_decrypt(c, seed)
print(p)
