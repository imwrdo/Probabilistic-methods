import random
from tabulate import tabulate

def giveX(num):
    licz = 0
    sum = 0
    prob = [0.5,0.2,0.2,0.1]
    for i in prob:
        sum+=i
        if(num < sum):
            return licz+1
        licz+=1
    return 4

def giveY(num,prob):
    licz = 0
    sum = 0
    for i in prob:
        sum+=i
        if(num < sum):
            return licz+1
        licz+=1
    return 4

def generate(randomNum):
    probY1 = [0.2,0,0,0.8]
    probY2 = [1,0,0,0]
    probY3 = [0,0.5,0,0.5]
    probY4 = [0,0,1,0]
    x = randomNum.random()
    xResult = giveX(x)
    if xResult == 1:
        y = randomNum.random()
        yResult = giveY(y,probY1)
    elif xResult == 2:
        y = randomNum.random()
        yResult = giveY(y,probY2)
    elif xResult == 3:
        y = randomNum.random()
        yResult = giveY(y,probY3)
    else:
        y = randomNum.random()
        yResult = giveY(y,probY4)
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
