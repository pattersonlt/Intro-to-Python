#Luke Patterson
#1-21-2014
#This program displays subtotal price of 5 items and the total price wiht sales tax

tax=.06 #Variable for tax

#Request user input of items
item1 = float(input('Enter the price of the first item:'))
item2 = float(input('Enter the price of the second item:'))
item3 = float(input('Enter the price of the third item:'))
item4 = float(input('Enter the price of the fourth item:'))
item5 = float(input('Enter the price of the fifth item:'))

#Calculate subtotal, sales tax, and the total
subtotal = item1 + item2 + item3 + item4 + item5
salestax = subtotal*tax
total = subtotal+salestax

#Print the information to the screen
print('The subtotal of the items is: $', format(subtotal,',.2f'), sep='')
print('The sales tax of the items is: $', format(salestax,',.2f'), sep='')
print('The total price of the items is: $', format(total,'.2f'), sep='')
