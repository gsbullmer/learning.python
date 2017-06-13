"""numbers.py"""


# integers
a = 12
b = 3
print(a + b)    # 15        # addition
print(b - a)    # -9        # subtraction
print(a // b)   # 4         # integer division
print(a / b)    # 4.0       # true division
print(a * b)    # 36        # multiplication
print(b ** a)   # 531441    # power operator
print(2 ** 1024)    # a very big number, Python handles it gracefully
# 1797693134862315907729305190789024733617976978942306572734300811577
# 3267580550096313270847732240753602112011387987139335765878976881441
# 6622492847430639474124377767893424865485276302219601246094119453082
# 9520850057688381506823424628814739131105408272371633505106845862982
# 39947245938479716304835356329624224137216


# integer and true division
print(7 / 4)    # 1.75  # true division
print(7 // 4)   # 1     # integer division, flooring returns 1
print(-7 / 4)   # -1.75 # true division again, result is opposite of previous
print(-7 // 4)  # -2    # integer div., result not the opposite of previous


# truncation towards 0
print(int(1.75))    # 1
print(int(-1.75))   # -1


# modulo operator
print(10 % 3)   # 1     # remainder of the division 10 // 3
print(10 % 4)   # 2     # remainder of the division 10 // 4


# booleans
print(int(True))    # 1     # True behaves like 1
print(int(False))   # 0     # False behaves like 0
print(bool(1))      # True  # 1 evaluates to True in a boolean context
print(bool(-42))    # True  # and so does every non-zero number
print(bool(0))      # False # 0 evaluates to False

# quick peak at the operators (and, or, not)
print(not True)         # False
print(not False)        # True
print(True and True)    # True
print(False or True)    # True

# boolean integers
print(1 + True)     # 2
print(False + 42)   # 42
print(7 - True)     # 6


# reals
pi = 3.1415926536   # how many digits of PI can you remember?
radius = 4.5
area = pi * (radius ** 2)
print(area)     # 63.61725123519331


# sys.float_info
import sys
print(sys.float_info)
# sys.float_info(max=1.7976931348623157e+308, max_exp=1024, max_10_exp=308,
# min=2.2250738585072014e-308, min_exp=-1021, min_10_exp=-307, dig=15,
# mant_dig=53, epsilon=2.220446049250313e-16, radix=2, rounds=1)


# approximation issue
print(3 * 0.1 - 0.3)    # 5.551115123125783e-17     # this should be 0!!!


# complex
c = 3.14 + 2.73j
print(c.real)   # 3.14  # real part
print(c.imag)   # 2.73  # imaginary part
print(c.conjugate())    # (3.14-2.73j)  # conjugate of A + Bj is A - Bj
print(c * 2)    # (6.28+5.46j)  # multiplication is allowed
print(c ** 2)   # (2.4067000000000007+17.1444j)     # power operation as well
d = 1 + 1j      # addition and subtraction as well
print(c - d)    # (2.14+1.73j)


# fractions
from fractions import Fraction
print(Fraction(10, 6))  # mad hatter?
# Fraction(5, 3)  # notice it's been reduced to lowest terms
print(Fraction(1, 3) + Fraction(2, 3))  # 1/3 + 2/3 == 3/3 == 1/1
# Fraction(1, 1)
f = Fraction(10, 6)
print(f.numerator)      # 5
print(f.denominator)    # 3


# decimal
from decimal import Decimal as D  # rename for brevity
print(D(3.14))      # pi, from float, so approximation issues
# Decimal('3.140000000000000124344978758017532527446746826171875')
print(D('3.14'))    # pi, from a string, so no approximation issues
# Decimal('3.14')
print(D(0.1) * D(3) - D(0.3))   # from float, we still have the issue
# Decimal('2.775557561565156540423631668E-17')
print(D('0.1') * D(3) - D('0.3'))   # from string, all perfect
# Decimal('0.0')
