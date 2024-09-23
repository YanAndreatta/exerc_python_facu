day = int(input())
month = int(input())
result = "sim"

if day <= 0 or day > 31:
    print(result)
if month <= 0 or month > 12:
    print(result)

if month == 2 and day > 28:
    print(result)

if (month == 2 or month == 4 or month == 6 or month == 9 or month == 11) \
        and day > 30:
    print(result)

print(result)
