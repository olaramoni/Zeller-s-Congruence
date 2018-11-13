def inputNumber(startRange, endRange, nameRange):   #Function to check whether an integer value is within  given range
    dayValid = False  # Boolean to create loop
    while dayValid == False:  # Creating while loop so that program repeats until a valid number is inputted
        try:
            inputtedValue = input("Please a {} between {} and {} as a number: ".format(nameRange, startRange, endRange))
            inputtedValue = int(inputtedValue)
            if startRange-1 < inputtedValue < endRange+1:
                return inputtedValue
            else:
                print("Please enter a number between {} and {}".format(startRange, endRange))
        except ValueError:
            print("That wasn't a number")

year=inputNumber(1582,9999, " year ")
if year%4==0:
    if year%100:
        if year%400==0:
            leapYear=True
        else:
            leapYear=False
month=inputNumber(3,14, " month ")
if month in thirtyDayMonths:
    endRange=30
elif month in thirtyOneDayMonths:
    endRange=31
else:
    if leapYear==True:
        endRange=29
    else:
        endRange=28
day=inputNumber(1,endRange, " day ")
