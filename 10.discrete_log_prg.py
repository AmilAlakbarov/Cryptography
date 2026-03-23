def discrete_log_prg(seed, p, g, bits_count):
    x = seed
    bits = []
    mid = (p - 1) // 2

    for _ in range(bits_count):
        x = pow(g, x, p)
        if x < mid:
            bits.append(1)
        else:
            bits.append(0)

    return bits


def bits_to_int(bits):
    value = 0
    for b in bits:
        value = value * 2 + b
    return value


p = 383
g = 2
seed = 137
bits = discrete_log_prg(seed, p, g, 32)
print(bits)
print(bits_to_int(bits))
