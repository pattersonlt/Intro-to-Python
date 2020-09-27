#******************************************************
#Luke Patterson                                       *
#2-11-2014                                            *
#Program displays monthly and annual automobile costs *
#******************************************************

def main():
    #User inputs loan payment, insurance, gas, oil, tires, maintenance
    loanPayment = float(input('Enter the monthly loan amount: '))
    insurance = float(input('Enter the monthly insurance amount: '))
    gas = float(input('Enter the monthly gas amount: '))
    oil = float(input('Enter the monthly oil amount: '))
    tires = float(input('Enter the monthly tires amount: '))
    maintenance = float(input('Enter the monthly maintenance amount: '))

    #Calculate monthly and annual cost
    monthlyPayment = loanPayment+insurance+gas+oil+tires+maintenance
    annualPayment = monthlyPayment*12

    print_totals(monthlyPayment, annualPayment)

def print_totals(monthlyPayment, annualPayment):
    #Print monthly and annual costs
    print('Total Monthly Expense: $', format(monthlyPayment, '7,.2f'), sep='')
    print('Total Annual Expense: $', format(annualPayment, '7,.2f'), sep='')



#Call functions
main()
