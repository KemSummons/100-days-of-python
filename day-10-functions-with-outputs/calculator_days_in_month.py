def is_leap(year):
    if year % 4 == 0:
        if year % 100 != 0:
            return True
        elif year % 400 == 0:
            return True
        else:
            return False
    else:
        return False


def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if 1 > month > 12:
        return "Invalid month entered."
    if is_leap(year) == False:
        return month_days[month - 1]
    else:
        if month == 2:
            return 29
        else:
            return month_days[month - 1]


year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
