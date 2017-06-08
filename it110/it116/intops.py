# This is a simple demo intops.py
import sys

# Step1 get a and b from the keyboard
#a = float(raw_input("please input a:\n"))
#b= float(raw_input("please input b:\n"))

a = float(sys.argv[1])
b = float(sys.argv[2])


#Step2
total = a + b
diff = a - b
prod = a * b
quot = a / b

rem = a % b
exp = a ** b

print str(a), " +", str(b), " = ", str(total)
print str(a), " -", str(b), " = ", str(diff)
print str(a), " *", str(b), " = ", str(prod)
print str(a), " /", str(b), " = ", str(quot)
print str(a), " %", str(b), " = ", str(rem)
print str(a), " ^", str(b), " = ", str(exp)
