#******************************************************************************************************************
# @purpose :Demonstrate LeapYear.
# @file  :LeapYear.py
# @author :ShalineeBhawnani
#*******************************************************************************************************************
def leap_year(year):
    if year % 4==0 and year % 100 !=0:
        print(year,'year is a Leap Year' )
        return True
    elif year % 400==0:
        print(year, 'year is a Leap Year')
        return True
    elif year % 100==0:
        print(year, 'year is not Leap Year')
        return False
    else:
        print(year, 'is Not Leap Year')
        return False
#year = int(input('Enter year: '))
#print(leap_year(year))