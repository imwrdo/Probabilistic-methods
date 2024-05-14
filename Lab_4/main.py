import random
from tabulate import tabulate

def generate(randomNum):
    x = randomNum.random()

    if x < 0.5:
        xResult = 1
    elif x < 0.7:
        xResult = 2
    elif x < 0.9:
        xResult = 3
    else:
        xResult = 4

    if xResult == 1:
        y = randomNum.random()
        if y < 0.2:
            yResult = 1
        else:
            yResult = 4
    elif xResult == 2:
        yResult = 1
    elif xResult == 3:
        y = randomNum.random()
        if y < 0.5:
            yResult = 2
        else:
            yResult = 4
    else:
        yResult = 3

    return xResult, yResult

def main():
    randomNum = random.Random()

    stats = [[0] * 4 for _ in range(4)]
    for _ in range(100000):
        xy = generate(randomNum)
        stats[xy[0] - 1][xy[1] - 1] += 1

    headers = ["XY", "1", "2", "3", "4"]
    table = [[str(x + 1)] + stats[x] for x in range(4)]

    print(tabulate(table, headers, tablefmt="grid"))

if __name__ == "__main__":
    main()
