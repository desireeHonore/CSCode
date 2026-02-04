"""
Name: Desiree F Honore
Email: Desiree.honore75@myhunter.cuny.edu
Resources: HackerRank
"""

leapyear = int(input("Enter a year between 1000 and 10000: "))

def is_leap(year):
    """This function finds out if an integer is considered a leap
        year by meeting the following conditions:"""
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False


if is_leap(leapyear):
    print(leapyear, " is a leap year!")
else:
    print(leapyear, "is not a leap year.")
