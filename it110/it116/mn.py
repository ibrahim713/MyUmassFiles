import sys
import random
n = 123456789
m= 0

print n, m

while n !=0:
    m = (10 * m) + (n %10)
n =n  / 10
    print m, n
