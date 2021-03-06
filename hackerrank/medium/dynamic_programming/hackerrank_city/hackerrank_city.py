M = 1000000007

N = int(input())

A = [int(w) for w in input().split()]

S = 0
L = 0

s0 = 1
s1 = 0
n = 0
for a in A:
    S = (4*S + 12*(s0*s1)%M + 16*a*(s0*s0)%M + 8*s1 + 12*a*s0 + a) % M

    S0 = 4*s0 + 2
    S1 = 4*s1 + (8*a + 3*L)*s0 + 2*L+3*a

    s0 = S0 % M
    s1 = S1 % M
    
    L = (2 * L + 3*a) % M

print(S)

# 12 x 1: 546992143  
# 12 x 2: 73820020 
# 13 x 1: 108424354 
# 13 x 2: 278277052 
# 14 x 1: 204746295 
# 20 x 1: 379289917 
# 20 x 2: 803630177 

# 2 7 2 3 9: 160136077 

