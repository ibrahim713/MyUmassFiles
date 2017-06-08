import random

#gonna use function and then return the result or call i back
def randomnumbers():
    print "Random numbers in a text file:"
    x = int(input("How many numbers do you want your file to have \n"))# input by u
    file=open('randomnumbers.txt', 'w')
    while x!=0: # when the count is not equal to zero
        num = random.randint(1,500)# numbers in range 1-500
        file.write(str(num)+'\n''') # have 1 number in each line
        x = x-1
        file.close
randomnumbers()
