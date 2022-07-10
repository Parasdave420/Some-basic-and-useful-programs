# Python3 code to calculate age in years
import datetime


def calculate_age(birthdate):
    today = datetime.date.today()
    try:
        age = birthdate.replace(year=today.year)

    # raised when birth date is February 29
    # and the current year is not a leap year
    except ValueError:
        age = birthdate.replace(year=today.year,month=birthdate.month + 1, day=1)

    if age > today:
        return today.year - birthdate.year - 1
    else:
        return today.year - birthdate.year


# Driver code
name = input("Enter your name: ")
birthday = input("Enter your birthdate in DD/MM/YYYY format: ")
try:
    DOB = datetime.datetime.strptime(birthday,"%d/%m/%Y").date()
    # print(calculate_age(DOB))
    print(f"Hey {name}!!! \nYour age is {calculate_age(DOB)}.")
except ValueError:
    print("Your entered birthdate is not correct")
