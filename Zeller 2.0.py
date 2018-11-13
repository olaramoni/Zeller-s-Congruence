daysOfWeek=["Saturday","Sunday","Monday","Tuesday","Wednesday","Thursday","Friday"]
thirtyOneDayMonths=[3,5,7,8,10,12,13]   #List of months with 31 days
thirtyDayMonths=[4,6,9,11]  #List of months with 30 days
leapYear=False #Boolean will help determine whether the year is a leap year or not

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
def calculateDay(day,month,year):
    dayOfWeek=(day+(13*(month+1)/5)+(year%100)+((year%100)/4)+((year//100)/4)-(2*(year/100)))%7
    return dayOfWeek
year=inputNumber(1582,9999, " year ")
if year%4==0:
    if year % 400 == 0 and year % 100 == 0:
        leapYear=True
    elif year % 400 != 0 and year % 100 == 0:
        leapYear=False
    else:
        leapYear=True
else:
    leapYear=False
month=inputNumber(3,14, " month ")
if month in thirtyDayMonths:
    endRange=30
elif month in thirtyOneDayMonths:
    endRange=31
else:
    if leapYear:
        endRange=29
    else:
        endRange=28
day=inputNumber(1,endRange, " day ")
total=calculateDay(day,month,year)
print(total)
print (daysOfWeek[int(str(total)[0])])