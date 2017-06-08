def readgolfile():

    file = open('golf.txt', 'r')

    name= file.readline()
    name= name.rstrip('\n')
    score=''
    while name!='':
        score=file.readline()
        print('Name:',name)
        print ('Score:',score)
        name=file.readline()
        name= name.rstrip('\n')

    file.close()

readgolfile()
