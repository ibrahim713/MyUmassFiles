import sys
# two variables v and t

t = float(sys.argv[1])
v = float(sys.argv[2])

w = 35.74 + 0.6215 * t + (0.4275 * t - 35.75) * v ** 0.16

if (t > 50):
    print ' Please enter a number lower than 50 for the 1st value'
elif (v > 120):
    print ' Please enter a number lower than 120 for the 2nd value'
elif (v < 3):
    print ' Please enter a number higher than 3 for the 2nd value'
else:
    print str(w)

