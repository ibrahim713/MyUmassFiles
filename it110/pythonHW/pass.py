import sys
p = raw_input('Please Enter Password:\n')

upper =0
lower = 0
digit= 0
symbol = 0
                                  
for i in p:                       
        if i.isupper() == True:   
                upper+=1          
        elif i.islower():          
                lower += 1       
        elif i.isdigit():        
                digit +=1        
        else:                    
                symbol +=1
if len(p) <8:
        print 'Weak Password'
        print 'Password needs to be 8 characters long'
elif upper >0 and lower>0 and symbol >0 and digit >0:
        print 'Strong Password'
else:
        print 'Weak Password, Need a symbol,upper case, lower case and number'
                                 

