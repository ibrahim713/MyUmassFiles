price1 = int(raw_input('Enter The 1st Price:'))
price2 = int(raw_input('Enter The 2nd Price:'))
price3 = int(raw_input('Enter The 3rd Price:'))
price4 = int(raw_input('Enter The 4th Price:'))
price5 = int(raw_input('Enter The 5th Price:'))

subtotal = price1 + price2 + price3 + price4 + price5

tax = subtotal * 0.7

print 'Your total is,' , subtotal, '. With the sales Tax it is', tax
