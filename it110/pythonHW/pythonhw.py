import re
textfile = open('mytextt.txt', 'r')
filetext = textfile.read()


match1 = re.findall("(\d{3}-\d{3}-\d{4})", filetext)

match2 = re.findall("(\(\d{3}\)-\d{3}-\d{4})", filetext)
print 'All Phones found in the File'
print match1, "\n"
print 'Another Phone format found'
print match2,"\n"
match3 = re.findall(r'[\w\.-]+@[\w\.-]+', filetext)
print 'All Emails found in The File'
print match3, "\n"
match4 = re.findall("(\d{5})", filetext)
print 'All Zip Codes found'
print match4, "\n"
print 'All Names Founds'
match5 = re.findall('(?P<name1>[A-Z]+)', filetext)
print match5, "\n"
textfile.close()
