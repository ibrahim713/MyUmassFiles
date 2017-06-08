
import sys
p = raw_input(("enter a password to check it's strength"))

if len (p) <= 8:
    if p.isupper() or p.islower() or int(p):
        print"This is a weak password  "
elif len(p) > 8 and len(p)  <26:
    if p.isupper() or p.islower() or isdigit():
        print "This is a Weak Password"
    else:
        print "Good Password"
