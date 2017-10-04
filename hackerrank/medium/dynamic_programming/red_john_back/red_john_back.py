import math

#F(0) = 1
#F(1) = 1
#F(2) = 1
#F(3) = 1
#F(4) = F(3) + F(0) = 2
#F(5) = 2 + 1 = 3
#F(6) = 4
#F(7) = 5
#F(N) = F(N-1) + F(N-4)

def f_gen():
    yield 1 # f1
    yield 1 # f2
    yield 1 # f3
    f0, f1, f2, f3 = 1, 1, 1, 1
    while True:
        f0, f1, f2, f3 = f1, f2, f3, f3+f0
        yield f3
        
def is_prime(n):
    if n <= 1:
        return False
    if n % 2 == 0 and n > 2: 
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

ntests = int(input())
tests = {}
for t in range(ntests):
    tests[t] = int(input())
    
N = set(tests.values())
max_n = max(N)
res = {}
n_primes = 0
lower = 1
n = 1
for fn in f_gen():
    if n > max_n:
        break
        
    if n in N:
        upper = fn
        for x in range(lower, upper+1):
            if is_prime(x):
                n_primes += 1
                
        lower = upper + 1
        res[n] = (fn, n_primes)
        
    n += 1
    
for t in range(ntests):
    n = tests[t]
    fn, n_primes = res[n]
    print(n_primes)

