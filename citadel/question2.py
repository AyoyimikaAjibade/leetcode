# 2. Prime Factor Visitation

# Alex entered a room with some fancy lights arranged in a row which were either on or off Alex had a list of numbers and worked through each number on that list in order. 
# For each number, Alex visited the bulbs at positions which were a multiple of the prime factors of the chosen number. Whenever a bulb was visited, its state was flipped. 
# Determine the final state of each bulb after the numbers on the list were processed.


# For example, given netobulbs, initially states 100110111, where means off and 1 means on and a list of m 3 numbers, numbers = [3, 4, 15]. 
# The states of the bulbs after processing each number are as follows, where a bolded state means this bulb's state was flipped.

# Initial state
# [11001101111]
# numbers[0]-3, there is one prime factor: (3). After the states are changed, affected bulbs in bold:
# [1101001011]
# numbers[1]-4, there is one prime factor: (2) The states of the bulbs and the affected bulbs are 
# [10111100001]
# numbers[2]-15, the prime factors are (3. 51. The states of the bulbs and the affected bulbs are
# [110011000101]
# [110010000111]

# The final states are 2001000011

# Function Description

# Complete the function lightBulbs in the editor below. The function must return an array of integers that denote the final states of each bulb.

# LightBulbs has the following parameter(s)
# states/states(1) states[n]) an array of nintegers that denote the initial states of each bulb
# numbers(numbers(0) numbers(m-1: an array of mintegers, the elements in her list

from math import sqrt

# get primes up to max(numbers)
def _getPrimes(n):
    ret = set(range(2, n + 1))
    for i in range(2, n + 1):
        if i in ret:
            j = i*2
            while j <= n:
                if j in ret:
                    ret.remove(j)
                j += i
    
    return ret

def _getPrimeFactors(n, primes):
    ret = set()
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            for d in (i, n // i):
                if d in primes:
                    ret.add(d)
    
    return ret

def primes(states, numbers):
    ma = max(max(numbers), len(states))
    primes = _getPrimes(ma)
    # if we see a prime factor an odd num of times, we
    # flip it. if not, we don't. we may flip more than once
    # even with this logic b/c we deal with multiples of primes
    allPrimes = set()
    for num in numbers:
        for p in _getPrimeFactors(num, primes):
            if p in allPrimes:
                allPrimes.remove(p)
            else:
                allPrimes.add(p)

    for i in range(len(states)):
        pos = i + 1
        pf = _getPrimeFactors(pos, primes)
        for p in pf:
            if p in allPrimes:
                states[i] = 1 - states[i]
    return states

### SOME AUTOMATED TESTING BELOW

def brute(states, numbers):
    primes = _getPrimes(max(numbers))
    for num in numbers:
        for p in _getPrimeFactors(num, primes):
            i = p
            while i <= len(states):
                states[i - 1] = 1 - states[i - 1]
                i += p
                
    return states
    
from random import randint
# has to be kinda small so the bruteforce works for testing
T = 100
N = 10**2
M = 10**2
V = 2 * 10**2
bad = 0
for _ in range(T):
    n = randint(1, N)
    m = randint(1, M)
    states = [randint(0, 1) for _ in range(n)]
    nums = [randint(1, V) for _ in range(m)]
    mine = primes(states, nums)
    actual = brute(states, nums)
    if mine != actual:
        bad += 1
print("Bad", bad)