class linearGenerator:
    def __init__(self,a,c,m,seed=15):
        self.a = a
        self.c = c
        self.m = m
        self.state = seed
    def algorytm(self):
        self.state = (self.a*self.state+self.c)%self.m
        return self.state / self.m
    def generate_sequence_linear(self,N):
        sequence = []
        for _ in range(N):
            sequence.append(self.algorytm())
        return sequence

class shiftGenerator:
    def __init__(self, p, q, m, seed=0b11010101000000000000000000000000):
        self.p = p
        self.q = q
        self.m = m
        self.state = seed
    
    def generate_sequence_shift(self):
        for i in range(23, -1, -1):
            new_bit = (self.state >> (i + self.p)) & 1 ^ (self.state >> (i + self.q)) & 1
            self.state ^= (-new_bit ^ self.state) & (1 << i)

        for i in range(30, 23, -1):
            self.state ^= ((self.state >> (i - 24)) & 1) << i

        return self.state / self.m

a = 69069
c = 1
m = 2**31
N = 100000

lcg = linearGenerator(a, c, m)
sequence_1 = lcg.generate_sequence_linear(N)

interval_1 = [0]*10
for num in sequence_1:
    index = int(num*10)
    interval_1[index] += 1
print("\nLinear generator")
for i, count in enumerate(interval_1):
    print(f"Interval {i+1}: {count}")

p = 7
q = 3


SGen = shiftGenerator(p, q, m)

interval_2 = [0]*10
for _ in range(N):
    newNum = SGen.generate_sequence_shift()
    interval_2[int(newNum * 10) % 10] += 1

print("\nShift generator")
for i, count in enumerate(interval_2):
    print(f"Interval {i+1}: {count}")
