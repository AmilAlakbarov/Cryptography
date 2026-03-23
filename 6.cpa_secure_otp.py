import hashlib
import hmac
import secrets


def keystream(key, nonce, length):
    out = b""
    counter = 0
    while len(out) < length:
        msg = nonce + counter.to_bytes(4, "big")
        out += hmac.new(key, msg, hashlib.sha256).digest()
        counter += 1
    return out[:length]


def encrypt(key, message_bytes):
    nonce = secrets.token_bytes(12)
    ks = keystream(key, nonce, len(message_bytes))
    body = bytearray()
    for i in range(len(message_bytes)):
        body.append(message_bytes[i] ^ ks[i])
    return nonce + bytes(body)


def decrypt(key, cipher_bytes):
    nonce = cipher_bytes[:12]
    body = cipher_bytes[12:]
    ks = keystream(key, nonce, len(body))
    msg = bytearray()
    for i in range(len(body)):
        msg.append(body[i] ^ ks[i])
    return bytes(msg)


key = secrets.token_bytes(32)
m = b"same text"
c1 = encrypt(key, m)
c2 = encrypt(key, m)
print(c1 != c2)
print(decrypt(key, c1))
