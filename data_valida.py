day = int(input())
month = int(input())
year = int(input())
result = "sim"


if day <= 0 or day > 31:
    result = "não"

if month <= 0 or month > 12:
    result = "não"

if month == 2 and day > 28:
    result = "não"

if (month == 4 or month == 6 or month == 9 or month == 11) and day > 30:
    result = "não"

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            bissexto = True
        else:
            bissexto = False
    else:
        bissexto = True
else:
    bissexto = False

if month == 2:
    if bissexto:
        if day <= 29:
            result = "sim"
        else:
            result = "não"
    else:
        if day <= 28:
            result = "sim"
        else:
            result = "não"
print(result)
