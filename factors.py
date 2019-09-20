# factors

from itertools import permutations
from sys import stdin

FACS = {}
PRIMES = {}
SMALLS = {}

def smallfac(n):
    if n in SMALLS:
        return SMALLS[n]
    for i in range(2,n//2):
        if n%i == 0:
            SMALLS[n] = i
            return i

def isprime(n):
    if n in PRIMES:
        return PRIMES[n]
    for i in range(2,n//2):
        if n%i == 0:
            PRIMES[n] = False
            return False
    PRIMES[n] = True
    return True

def factor(n):
    if n in FACS:
        return FACS[n]
    temp = n
    facs = []
    while not isprime(temp):
        fac = smallfac(temp)
        facs.append(fac)
        temp = temp//fac
    facs.append(temp)
    f = len(set(permutations(facs)))
    FACS[n] = f
    return f


for line in stdin.readlines():
    if line == "\n":
        break
    
    n = int(line)

    x = 2
    while(factor(x) < n):
        if x%100 == 0:
            print(x)
        x += 1

    print(f'{n} {x}')
