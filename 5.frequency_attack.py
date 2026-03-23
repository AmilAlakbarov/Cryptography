def decrypt_caesar(text, shift):
    out = ""
    for ch in text:
        if ch.isalpha():
            if ch.isupper():
                base = ord("A")
            else:
                base = ord("a")
            out += chr((ord(ch) - base - shift) % 26 + base)
        else:
            out += ch
    return out


def score_text(text):
    common = "etaoin"
    s = 0
    low = text.lower()
    for ch in low:
        if ch in common:
            s += 1
    return s


def frequency_attack_caesar(cipher_text):
    best_shift = 0
    best_plain = ""
    best_score = -1

    for shift in range(26):
        plain = decrypt_caesar(cipher_text, shift)
        sc = score_text(plain)
        if sc > best_score:
            best_score = sc
            best_shift = shift
            best_plain = plain

    return best_shift, best_plain


c = "wklv lv d vhfuhw"
shift, text = frequency_attack_caesar(c)
print(shift, text)
