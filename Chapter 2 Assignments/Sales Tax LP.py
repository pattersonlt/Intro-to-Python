#*******************************************
#Name:      Luke Patterson                 *
#Date:      1/23/2014                      *
#Purpose:   Prints and calculates          *
#           tax amounts and final price    *
#*******************************************

#Declare tax variables
stateTax = .04
countyTax = .02

#User inputs price
purchase = float(input('Enter the amount of the purchase: '))

#Calculate tax amounts
stateTaxAmount = purchase*stateTax
countyTaxAmount = purchase*countyTax
total = purchase+stateTaxAmount+countyTaxAmount

#print purchase, tax amounts, and total
print('Purchase:    $', format(purchase, '7,.2f'))
print('State Tax:   $', format(stateTaxAmount, '7,.2f'))
print('County Tax:  $', format(countyTaxAmount, '7,.2f'))
print('Total Price: $', format(total, '7,.2f'))



