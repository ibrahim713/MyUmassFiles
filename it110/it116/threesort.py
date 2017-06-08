import sys

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

minValue = min(min(a,b),c)
maxValue = max(max(a,b),c)
middleValue = a + b + c - minValue - maxValue

print minValue, middleValue, maxValue
