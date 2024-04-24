import random

def transform_1(n):
    return n * 100 + 50

def transform_2(n):
    if n < 0.1:
        return 1
    if n < 0.3:
        return 2
    if n < 0.6:
        return 3
    return 4

def main():
    arr = []
    count = {}

    for _ in range(100000):
        num = random.random()
        proc = transform_1(num)
        arr.append(proc)

    for level in range(10):
        range_ = (50 + (10 * level), 50 + (10 * level) + 10)
        count[range_] = 0

    for n in arr:
        for i in range(10):
            range_ = (50 + (10 * i), 50 + (10 * i) + 10)
            if n >= range_[0] and n <= range_[1]:
                count[range_] += 1
                break

    for i in range(10):
        range_ = (50 + (10 * i), 50 + (10 * i) + 10)
        print(f"({range_[0]}, {range_[1]}): {count[range_]}")

    print()
    arr.clear()
    count2 = [0, 0, 0, 0]

    for _ in range(100000):
        num = random.random()
        val = transform_2(num)
        arr.append(val)
        count2[val - 1] += 1

    for i in range(4):
        print(f"{i+1}: {count2[i]}")

if __name__ == "__main__":
    main()
