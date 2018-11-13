import tkinter
window=tkinter.Tk()
dayLabel=tkinter.Label(window, text="Day:")
dayLabel.pack()
dayEntry=tkinter.Entry()
dayEntry.pack()
monthLabel=tkinter.Label(window, text="Month:")
monthLabel.pack()
monthEntry=tkinter.Entry()
monthEntry.pack()
yearLabel=tkinter.Label(window, text="Year:")
yearLabel.pack()
yearEntry=tkinter.Entry()
yearEntry.pack()
calculateButton=tkinter.Button(window, text="Calculate day")
calculateButton.pack()
window.mainloop()
def inputYear(startRange, endRange, nameRange):   #Function to check whether an integer value is within  given range
    dayValid = False  # Boolean to create loop
    while dayValid == False:  # Creating while loop so that program repeats until a valid number is inputted
        try:
            inputtedValue = yearEntry.get()
            inputtedValue = int(inputtedValue)
            if startRange-1 < inputtedValue < endRange+1:
                return inputtedValue
            else:
                print("Please enter a number between {} and {}".format(startRange, endRange))
        except ValueError:
            print("That wasn't a number")
def inputMonth(startRange, endRange, nameRange):   #Function to check whether an integer value is within  given range
    dayValid = False  # Boolean to create loop
    while dayValid == False:  # Creating while loop so that program repeats until a valid number is inputted
        try:
            inputtedValue = monthEntry.get()
            inputtedValue = int(inputtedValue)
            if startRange-1 < inputtedValue < endRange+1:
                return inputtedValue
            else:
                print("Please enter a number between {} and {}".format(startRange, endRange))
        except ValueError:
            print("That wasn't a number")
def inputDay(startRange, endRange, nameRange):   #Function to check whether an integer value is within  given range
    dayValid = False  # Boolean to create loop
    while dayValid == False:  # Creating while loop so that program repeats until a valid number is inputted
        try:
            inputtedValue = dayEntry.get()
            inputtedValue = int(inputtedValue)
            if startRange-1 < inputtedValue < endRange+1:
                return inputtedValue
            else:
                print("Please enter a number between {} and {}".format(startRange, endRange))
        except ValueError:
            print("That wasn't a number")
def calculateDay(day,month,year):
    dayOfWeek=(day+(13*(month+1)/5)+(year%100)+((year%100)/4)+((year//100)/4)-(2*(year//100)))%7
    return dayOfWeek

year=inputYear(1582,9999, " year ")
if year%4==0:
    if year%100:
        if year%400==0:
            leapYear=True
        else:
            leapYear=False
month=inputMonth(3,14, " month ")
if month in thirtyDayMonths:
    endRange=30
elif month in thirtyOneDayMonths:
    endRange=31
else:
    if leapYear==True:
        endRange=29
    else:
        endRange=28
day=inputDay(1,endRange, " day ")
