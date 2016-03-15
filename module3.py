#-------------------------------------------------------------------------------
# Name:        module3
# Purpose:
#
# Author:      Owner
#
# Created:     27/12/2015
# Copyright:   (c) Owner 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()


# Given your birthday and the current date, calculate your age
# in days. Compensate for leap days. Assume that the birthday
# and current date are correct dates (and no time travel).
# Simply put, if you were born 1 Jan 2012 and todays date is
# 2 Jan 2012 you are 1 day old.

daysOfMonths = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
daysOfLeapYear = [ 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def isLeapYear(year):
    ##
    # Your code here. Return True or False
    # Pseudo code for this algorithm is found at
    # http://en.wikipedia.org/wiki/Leap_year#Algorithm
    ##
    if year%4 != 0:
        return False
    elif year%100 != 0:
        return True
    elif year%400 != 0:
        return False
    else:
        return True

def nextDay(year, month, day):
    """
    Returns the year, month, day of the next day.
    Simple version: assume every month has 30 days.
    """
    # YOUR CODE HERE
    if day%30 == 0:
        day = 1
        if month%12 == 0:
            month = 1
            year+= 1
        else:
            month+= 1
    else:
        day += 1

    return (year,month,day)

def equalDates(year1,month1,day1,year2,month2,day2):
    """" Return a boolean. Compare two dates and tell
        if they are equal
    """
    return year1 == year2 and month1 == month2 and day1 == day2

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar, and the first date is not after
       the second."""

    days = 0

    while True:
        if equalDates(year1,month1,day1,year2,month2,day2):
            break
        else:
            days+= 1
            year1,month1,day1 = nextDay(year1,month1,day1)

    return days


def test():
    test_cases = [((2012,9,30,2012,10,30),30),
                  ((2012,1,1,2013,1,1),360),
                  ((2012,9,1,2012,9,4),3)]

    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        print(result)
        if result != answer:
            print("Test with data:", args, "failed")
        else:
            print("Test case passed!")

test()


##def daysBetweenDates(y1, m1, d1, y2, m2, d2):
##    ##
##    # Your code here.
##    days_year = sum(daysOfMonths)
##
##    days = 0
##
##    if y2 == y1:
##        num_years = 0
##    else:
##        num_years = y2 - y1 -1
##
##    if isLeapYear(y1):
##        days_in_birthmonth = daysOfLeapYear[m1-1] - d1
##        days_in_birthyear =  sum(daysOfLeapYear[m1:])
##    else:
##        days_in_birthmonth = daysOfMonths[m1-1] - d1
##        days_in_birthyear =  sum(daysOfMonths[m1+1:])
##
##    if isLeapYear(y2):
##        days_in_cmonth = sum(daysOfLeapYear[:m2-1])
##    else:
##        days_in_cmonth = sum(daysOfMonths[:m2-1])
##
##    days_in_years = num_years * days_year
##    days = days_in_birthmonth + days_in_birthyear + days_in_years + days_in_cmonth \
##            + d2
##
##    for i in range(y1+1,y2):
##        if isLeapYear(i):
##            days+= 1
##    ##
##    return days
##
##print(daysBetweenDates(2000, 2, 15, 2000, 2, 22))
