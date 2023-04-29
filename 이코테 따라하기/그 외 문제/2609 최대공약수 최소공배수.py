def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

a, b = map(int, input().split()) 
gcdnum = gcd(a, b)
lcmnum = a * b // gcdnum

print(gcdnum)
print(lcmnum)