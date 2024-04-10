class LCGGenerator:
    def __init__(self,a,c,m,seed=1  ):
        self.a = a
        self.c = c
        self.m = m
        self.state = seed
    def algorytm(self):
        self.state = ( self.a * self.state + self.c ) % self.m
        return self.state / self.m
    def generate_sequence(self,N):
        sequence = []
        for _ in range(N):
            sequence.append(self.algorytm())
        return sequence

class shiftRegister:
    def __init__(self, N, p, q,seed = 1234):
        self.N = N
        self.p = p
        self.q = q
        self.state = seed
        
    def SRGen(self):
        if self.N <= 0:
            return None
        
        self.state = list(map(int, bin(self.state)[2:]))    
        if len(self.state) < self.p:
            self.state = self.state + self.state
        randomSequence = []
        
        for i in range(self.N):
            if(i<self.p):
                randomSequence.append(self.state[i])
            else: 
                randomSequence.append(randomSequence[i-self.p] ^ randomSequence[i-self.q])
        return randomSequence
    

a = 16807
c = 0
m = 2**31 - 1
N = 1000000

lcg = LCGGenerator(a,c,m)




sequence_1 = lcg.generate_sequence(N)
intervals = [0]*10
for num in sequence_1:
    index = int(num*10)
    intervals[index]+=1
    
for i,count in enumerate(intervals):
    print(f"Przedzial {i}: {count}")
    
p = 10
q = 3

SRgenerator = shiftRegister(N,p,q)

sequence_2 = SRgenerator.SRGen()
intervals_2 = [0]*2
for num in sequence_2:
    index = int(num)
    intervals_2[index]+=1
    
for i,count in enumerate(intervals_2):
    print(f"Przedzial {i}: {count}")
