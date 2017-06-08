#chaos

import sys
print("this is chaotic function")
x =float(input("Enter a number between 0 and 1:\n"))
for i in range(100):
      x = 3.8* x * (1-x)
      print (x)
