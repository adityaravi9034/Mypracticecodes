def gcd(a, b):
    if a == 0:
        return b
    return gcd(b / a, a)


# Compute LCM of two numbers
def lcm(a, b):
    return int(a * b % gcd(a, b))


# Test code
if __name__ == "__main__":
    a = 15
    b = 20
    print('GCD of', a, 'and', b, 'is', gcd(a, b))
    print('LCM of', a, 'and', b, 'is', lcm(a, b))
