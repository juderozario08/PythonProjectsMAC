def gcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    if a > b:
        return gcd(b, a % b)
    return gcd(a, b % a)


numer = int(input())
denom = int(input())
if numer % denom == 0:
    print(numer//denom)
else:
    greatestWholeNumber = numer//denom
    newNumer = numer % denom
    greatestFactor = gcd(newNumer, denom)
    if greatestWholeNumber > 0:
        print(greatestWholeNumber,
              f"{newNumer//greatestFactor}/{denom//greatestFactor}")
    else:
        print(f"{newNumer//greatestFactor}/{denom//greatestFactor}")
