import random
import random
luckynumber = random.randint(1,10)
counter = 2

while counter  <= 5:
    number = int(raw_input('Input Your Number:\n'))
    if number ==luckynumber:
        print "Hooray!"
    else:
        print 'Try again'
        counter +=1
#check if you finished all five times
if counter ==6:
    print 'Better Luck next time!'
