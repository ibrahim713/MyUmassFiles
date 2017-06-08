#demo prints out and save pascals traingle series
#only prints out first 10 lines. or u can increase range(10)


f =open('output.txt', 'a')
print >> f, 'Result'

list =[1]
for i in range(10):
        print(list)
        newlist = []
        newlist.append(list[0])
        for i in range(len(list) - 1):
            newlist.append(list[i] +list[i+1])
        newlist.append(list[-1])
        list = newlist
        print >> f, list

f.close()
