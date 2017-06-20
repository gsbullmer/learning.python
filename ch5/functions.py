def gcd(a, b):
    """Calculates the Greatest Common Divisor of (a, b). """
    while b != 0:
        a, b = b, a % b
    return a
