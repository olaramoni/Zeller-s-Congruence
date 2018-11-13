def inputYear():
    yearValid = False
    while yearValid == False:
        try:
            year = input("Please enter the year: ")
            year = int(year)
            if year > 0:
                return year
            else:
                print("Please enter a positive number: ")
        except ValueError:
            print("That was not a number")
