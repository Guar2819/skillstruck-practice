year = int(input("What year?"))

def leap_year(choice):
    if choice % 4 == 0 and choice % 100 !=0:
        print("Leap year!")
    else:
        print("Not a leap year.")



leap_year(year)