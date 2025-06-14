def is_leap_year(year):
    """Take a year input and return it if the year is a year leap or not"""
    # Write your code here. 
    # Don't change the function name.

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
is_leap_year(2024)

