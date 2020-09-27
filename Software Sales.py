def main():
    quantity = int(input("Enter the number of packages purchased: "))
    
    #Determine discount
    if quantity >= 10 and quantity <=19: 
                    discount = .2
    elif quantity >= 20 and quantity <= 49:
                    discount = .3
    elif quantity >= 50 and quantity <= 99:
                    discount = .4
    elif quantity >= 100:
                    discount = .5
    else:
                    discount = 0

    #pass quantity and discount to calculations
    calculations(quantity, discount)
                   
def calculations(quantity, discount):

    discountAmount =int(((quantity*99)*discount))

    totalAmount = int((quantity*99) - discountAmount)

    print('Discount Amount: $', format(discountAmount, '7,.2f'), sep = '')
    print('Total Amount: $', format(totalAmount, '7,.2f'), sep = '')
                   
main()
