def inputNumber(startRange, endRange):
    dayValid = False  # Boolean to create loop
    while dayValid == False:  # Creating loop
        try:
            inputtedValue = input("Please a value between {} and {} as a number: ".format(startRange, endRange))
            inputtedValue = int(inputtedValue)
            if startRange < inputtedValue < endRange+1:
                return inputtedValue
            else:
                print("Please enter a number between {} and {}".format(startRange, endRange))
        except ValueError:
            print("That wasn't a number")
inputNumber(1,31)