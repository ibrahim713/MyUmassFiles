# demo for ISBN

# step 1 get the input data
import sys

number = int(sys.argv[1])

originalNumber = number
checkDigit = 0
singleDigit = 0

# step 2 get the weightedSum from number
totalSum = 0
for i in range(2, 11):
      singleDigit = number % 10  # singleDigit from right side
      totalSum += i * singleDigit  # update the totalSum 
      number = number // 10

# step 3 get the final check digit

if totalSum % 11 == 10:
      checkDigit = 'X'
elif totalSum % 11 == 0:
      checkDigit = '0'
else:
      checkDigit = totalSum % 11

print 'Final ISBN number is: ', str(originalNumber) + str(checkDigit)


      
      
