import sys

m = int(sys.argv[1])
d = int(sys.argv[2])
y = int(sys.argv[3])

# y0 x m0 and d0
y0 = y - (14-m) // 12
x = y0 +y0 // 4 - y0 // 100 +y0 // 400
m0 = m + 12 * ((14- m) // 12) - 2
d0 = (d + x + (31 * m0) // 12) % 7

if (d0 == 0):
    print 'Sunday'

if (d0 == 1):
    print 'Monday'

if (d0 == 2):
    print 'Tuesday'

if (d0 == 3):
    print 'Wedsnday'

if (d0== 4):
    print 'Thrusday'

if (d0 == 5):
    print 'Friday'

if (d0 == 6):
    print 'Saturday'

