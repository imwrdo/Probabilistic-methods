import random

def zad_1(n,min,max):
    return n * (max - min) + min

def zad_2(num):
    licz = 0
    sum = 0
    prob = [0.05,0.15,0.25,0.55]
    for i in prob:
        sum+=i
        if(num<sum):
            return licz+1
        licz+=1
    return 4

def main():
    arr = []
    count = {}
    min = 50
    max = 150
    for _ in range(100000):
        num = random.random()
        proc = zad_1(num,min,max)
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
    print("First task:")
    for i in range(10):
        range_ = (50 + (10 * i), 50 + (10 * i) + 10)
        print(f"({range_[0]}, {range_[1]}): {count[range_]}")

    print()
    arr.clear()
    count2 = [0, 0, 0, 0]

    for _ in range(100000):
        num = random.random()
        val = zad_2(num)
        arr.append(val)
        count2[val - 1] += 1
    print("Second task:")
    for i in range(4):
        print(f"{i+1}: {count2[i]}")

if __name__ == "__main__":
    main()
