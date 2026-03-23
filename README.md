# Crypto Assignment (IT2024)

This repository contains 10 small Python implementations. I kept the code simple and direct, so each task is easy to read.

## 1) GCD
File: `1.gcd.py`
- Uses Euclid algorithm.
- Repeats `a, b = b, a % b` until `b = 0`.
- Final `a` is the gcd.

## 2) Ceaser and Affine ciphers
File: `2.ceaser_affine.py`
- Ceaser cipher shifts letters by a fixed value.
- Affine cipher uses:
  - Encrypt: `E(x) = (a*x + b) mod 26`
  - Decrypt: `D(y) = a_inv*(y-b) mod 26`
- Checks that `a` is coprime with 26.

## 3) OTP
File: `3.otp.py`
- Generates random key bytes with same length as message.
- Encrypt/decrypt using XOR byte by byte.
- OTP decryption is same XOR process.

## 4) OTP + PRG
File: `4.otp_prg.py`
- Uses a short random seed.
- Expands seed with SHA-256 + counter to get keystream.
- XOR with message for encryption/decryption.

## 5) Frequency analysis attack
File: `5.frequency_attack.py`
- Attacks Ceaser ciphertext.
- Tries all 26 shifts.
- Scores each candidate by common English letters.
- Picks best score as guessed plaintext.

## 6) CPA-secure OTP style
File: `6.cpa_secure_otp.py`
- Random nonce is generated every encryption.
- Keystream is made with HMAC-SHA256(key, nonce || counter).
- Ciphertext format: `nonce || (message XOR keystream)`.
- Same plaintext gives different ciphertext each time.

## 7) Extended Euclidean algorithm
File: `7.extended_euclid.py`
- Returns `(g, x, y)` such that `a*x + b*y = g`.
- Uses this to compute modular inverse when `gcd(a, m) = 1`.

## 8) RSA encryption scheme
File: `8.rsa.py`
- Picks small random primes `p, q`.
- Computes `n`, `phi`, chooses `e`, computes `d`.
- Encrypt: `c = m^e mod n`
- Decrypt: `m = c^d mod n`
- Educational version only (small primes).

## 9) Diffie-Hellman key exchange
File: `9.diffie_hellman.py`
- Public values: `p` and `g`.
- Each side chooses private key and sends public key.
- Both compute same shared secret using modular exponentiation.

## 10) PRG based on discrete-log
File: `10.discrete_log_prg.py`
- State update each round: `x = g^x mod p`.
- Outputs bits by comparing state to midpoint.
- Includes helper to convert bit list to integer.

## Run
Use Python 3:

- `python 1.gcd.py`
- `python 2.ceaser_affine.py`
- ...
- `python 10.discrete_log_prg.py`
