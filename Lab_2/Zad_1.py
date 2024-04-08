class LCGGenerator:
    def __init__(self, a, c, m, seed=1):
        self.a = a
        self.c = c
        self.m = m
        self.state = seed

    def next(self):
        self.state = (self.a * self.state + self.c) % self.m
        return self.state / (self.m - 1)  

    def generate_sequence(self, N):
        sequence = []
        for _ in range(N):
            sequence.append(self.next())
        return sequence

# Parametry generatora
a = 16807
c = 0
m = 2**31 - 1
N = 100000

# Tworzenie generatora
lcg = LCGGenerator(a, c, m)

# Generowanie ciągu liczb
sequence = lcg.generate_sequence(N)

# Podział zakresu na 10 części
intervals = [0] * 10
for num in sequence:
    index = int(num * 10)
    intervals[index] += 1


for i, count in enumerate(intervals):
    print(f"Przedział {i}: {count} liczb")

