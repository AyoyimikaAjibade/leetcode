# 3. Odd Strings
# We have an array of strings. Consider each string as a zero- indexed array of characters. 
# All of the characters will be in the range ascii[a-z] which have decimal values in the range [97-122]. 
# These decimal values are called ordinal values and will be referred to as ord[a]=97 for example.

# Given an array of strings s = [s[0].s[1]....s[n-1]], and an integer m, we calculate a value of each s[i] of length len(s[i]) as:

# value[i]=ord[s[i][0]]" x ord[s[i][1]]" x ... * 
# ord[s[i][len(s[i])-17m

# Perform the calculation on each string, sum them up and print whether their sum is EVEN or ODD.

# For example, your array s = ['abc', 'abcd']. It has k=2 strings. 
# Rewritten as a two-dimensional array of decimal ordinals, 
# we have s' = [[97,98,99],[97,98,99,100]]. If our exponent m-2 we perform the following:

from collections import Counter

def getRemainder(base, exponent, cache):
    if (base, exponent) in cache:
        return cache[(base, exponent)]

    l = base % 10
    if l in [0, 1, 5]:
        cache[(base, exponent)] = l
        return l

    rem = exponent % 4
    if rem == 0:
        if l in [2, 4, 6, 8]:
            cache[(base, exponent)] = 6
            return 6
        elif l in [3, 7, 9]:
            cache[(base, exponent)] = 1
            return 1
    else:
        l_power_rem = l**rem
        cache[(base, exponent)] = l_power_rem % 10
        return l_power_rem % 10


def getUnitPlace(string_ip):
    unitsplaces = []

    for eachChar in string_ip:
        unitsplaces.append(ord(eachChar) % 10)

    return unitsplaces


def getUnitPlaceOptimized(string_ip):
    charFreq = Counter(string_ip)
    unitsplacesFreqMap = {}
    for char, freq in charFreq.items():
        unitsplacesFreqMap[ord(char) % 10] = freq
    return unitsplacesFreqMap

def getStringCharProductOptimized(unitsPlaceFreqMap, m):
    cache = {}
    units = [getRemainder(unit, freq*m, cache) for unit, freq in unitsPlaceFreqMap.items()]
    output = 1
    for each in units:
        output *= each

    return output



def getStringCharProduct(unitsplaces, m):
    units = [ getRemainder(unit, m) for unit in unitsplaces]
    output = 1
    for each in units:
        output *= each

    return output

def solveOptimized(m, s):
    ordBases = [ getUnitPlaceOptimized(word) for word in s ]
    movingSum = 0
    for eachMap in ordBases:
        movingSum += getStringCharProductOptimized(eachMap, m)

    if movingSum % 2 == 0:
        return "EVEN"
    else:
        return "ODD"


def solve(m, s):
    ordBases = [ getUnitPlace(word) for word in s ] # ROOM for optimization, for repeating charcters create a map and possible m

    movingSum = 0

    for eachBase in ordBases:
        movingSum += getStringCharProduct(eachBase, m)

    if movingSum % 2 == 0:
        return ("EVEN")
    else:
        return ("ODD")


print(getRemainder(2014, 2012))
print(getRemainder(3, 34))
print(getRemainder(1453, 71))
print(getRemainder(2, 51))
print(getRemainder(6, 2021))
print(getRemainder(27, 20))

print("NORMAL APPROACH")
print(solve(3, ["aceace", "ceceaa", "abdbdbdbakjkljhkjh"]))
print(solve(3, ["azbde", "abcher", "acegk"]))
print(solve(36, ['wmgkeiaaieskieiacwkqcgkaiamqeqmekcocukeucoueh', 'gaikkkkmocqmkmogiceawiwgoggex', 'wcqeiooikqoiesukqcqgegkuqqgmeiakikikicsiegowacuqamceigamumgqumescgoakcqoaiimweeg', 'mimwaiwowikigmme', 'ocueqqiqikwwuscqoeaqsaeaaescb', 'siiwqumqcsksmuemkaikcagqgsekk', 'wqcgkscwmwcguwqowciagcesmgeagwkcoccmkgiskkawn', 'uggcqkqqeocsagoqmeuuquoqqsqst', 'ekquikkikiawiqwqouqmuaoqouegwowcueeccwqqwcccs', 'csgqgqcq', 'cueswewawuwqigkmkgkqusiukaouakqcceoiuammkskil']))

print("Optimized")

print(solveOptimized(3, ["aceace", "ceceaa", "abdbdbdbakjkljhkjh"]))
print(solveOptimized(3, ["azbde", "abcher", "acegk"]))
print(solveOptimized(36, ['wmgkeiaaieskieiacwkqcgkaiamqeqmekcocukeucoueh', 'gaikkkkmocqmkmogiceawiwgoggex', 'wcqeiooikqoiesukqcqgegkuqqgmeiakikikicsiegowacuqamceigamumgqumescgoakcqoaiimweeg', 'mimwaiwowikigmme', 'ocueqqiqikwwuscqoeaqsaeaaescb', 'siiwqumqcsksmuemkaikcagqgsekk', 'wqcgkscwmwcguwqowciagcesmgeagwkcoccmkgiskkawn', 'uggcqkqqeocsagoqmeuuquoqqsqst', 'ekquikkikiawiqwqouqmuaoqouegwowcueeccwqqwcccs', 'csgqgqcq', 'cueswewawuwqigkmkgkqusiukaouakqcceoiuammkskil']))