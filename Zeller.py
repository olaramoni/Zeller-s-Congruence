
dayValid=False #Boolean to create loop
while dayValid==False: #Creating loop
    try:
        day = input("Please enter the day of the month as a number: ")
        day=int(day)
        if 0<day<32:
            dayValid=True
        else:
            print("Please enter a number between 1 and 31")
    except ValueError:
        print("That wasn't a number")

monthValid = False
print(
    "March=3, April=4, May=5, June=6, July=7, August=8, September=9, October=10, November=11, December=12, January=13, February=14")
while monthValid == False:
    try:
        month = input("Please enter the number corresponding to the month you want: ")
        month = int(month)
        if 2 < month < 15:
            monthValid = True
        else:
            print("Please enter a number between 3 and 14")
    except ValueError:
        print("That was not a number")


yearValid = False
while yearValid == False:
    try:
        year = input("Please enter the year: ")
        year = int(year)
        if year > 0:
            yearValid = True
        else:
            print("Please enter a positive number: ")
    except ValueError:
        print("That was not a number")

a = (13 * (month + 1)) / 5  # first part of equation
centuryYear = (year % 100) / 4  # Calculating year of century
century = (year // 100) / 4  # Calculating the century
d = 2 * (year // 100) - 1  # Value that is double the century
total = day + a + century + centuryYear - d
total = total % 7
total = str(total)
daysOfWeek = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
print(total)
print(daysOfWeek[int(total[0])])
