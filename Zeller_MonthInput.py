def inputMonth()
    monthValid = False
    print(
        "March=3, April=4, May=5, June=6, July=7, August=8, September=9, October=10, November=11, December=12, January=13, February=14")
    while monthValid == False:
        try:
            month = input("Please enter the number corresponding to the month you want: ")
            month = int(month)
            if 2 < month < 15:
                return month
            else:
                print("Please enter a number between 3 and 14")
        except ValueError:
            print("That was not a number")