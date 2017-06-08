
# u must declare and ask python how to use it
def happyBirthdayEmily():
    print ("Happy Birthday Emily")
happyBirthdayEmily()

def hello():
    print'hellow world'
hello()

def times(x,y):
    return x*y

#def intersect(list1, list2):
#    list1=[SPAM]
#    list2=[SPAM]
#    return [element for element in list1 if element in list2]

def intersect(s1,s2):
    result=[]
    for item in s1:
        if item in s2:
            result.append(item)
    print result
intersect("SPAM","SCAM")

def intersect(s1,s2):
    result = [element for element in s1 if element in s2]
    print result
intersect("HELLO","HELL",)
