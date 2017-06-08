
def readrandomfile():
    file=open('randomnumbers.txt', 'r')
    total=0
    x=0
    print "Reading the File"
    for line in file:
        z = int(line)
        print("The random numbers:",z)
        total=total +z
        x=x+1
    file.close()
    print("Sum of the NUmbers is", total)
    print ("Random numbers", x)
readrandomfile()
