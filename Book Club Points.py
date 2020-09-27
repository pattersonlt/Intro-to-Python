def main():

    #variable to hold points
    
    
    #get number of books purchased
    booksPurchased = int(input("Enter the number of books purchased: "))

    #Determine number of points
    if booksPurchased == 0:
        points = 0
    elif booksPurchased == 1:
        points = 5
    elif booksPurchased == 2:
        points = 15
    elif booksPurchased == 3:
        points = 30
    elif booksPurchased >= 4:
        points = 60

    #display points awarded
    print(points, "points earned")

main()
