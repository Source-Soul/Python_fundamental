user_input = int(input("Enter a number: "))

def is_leap_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print(f"{year} is a leap year")
        return True
    return False

is_leap_year(user_input)