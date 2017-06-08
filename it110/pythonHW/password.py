mport sys
p = raw_input(("enter a password to check it's strength"))

if len (p) <= 8:
    if p.isupper() or p.islower():
        print"This is a weak password  "
elif len(p) > 8 and len(p)  <26:
    if p.isupper() or p.islower() or isdigit():
        print "Weak Ass Password Bro"
    else:
        print "Good Password"
