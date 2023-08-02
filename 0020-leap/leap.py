def leap_year(year):
    if (year % 100 == 0 and year % 400 != 0) or year % 4 !=0:
        return False
    return True
        