def shift_register_generator(seed, negated_bits):
    register = seed.copy()
    output = []

    for _ in range(100):
        feedback = sum(register[i] for i in negated_bits) % 2
        output.append(register[-1])
        register = [feedback] + register[:-1]

    return output[-31:]

def number_classification(data, M):
    classific = {str(i): 0 for i in range(10)}
    for numb in data:
        res = (numb * 10) // M
        classific[str(res)] += 1
    return classific

def binary_to_decimal(bits):
    return int(''.join(map(str, bits)), 2)

if __name__ == "__main__":
    m = 2 ** 31
    seed = [1, 0, 0, 1, 1, 0, 1]
    taps = [6, 2]

    N = 100000
    data2 = []
    for _ in range(100000):
        bits = shift_register_generator(seed, taps)
        numb = binary_to_decimal(bits)
        data2.append(numb)
        seed = bits[-7:]

    classific = number_classification(data2, m)
    print(classific)
