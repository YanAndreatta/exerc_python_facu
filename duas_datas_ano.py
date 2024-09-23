day_1 = int(input())
month_1 = int(input())
day_2 = int(input())
month_2 = int(input())

if month_1 < month_2:
    print(f"{day_1:02d}/{month_1} - {day_2:02d}{month_2}")
elif month_1 > month_2:
    print(f"{day_2:02d}/{month_2} - {day_1:02d}{month_1}")
else:
    if day_1 < day_2:
        print(f"{day_1:02d}/{month_1} - {day_2:02d}/{month_2}")
    else:
        print(f"{day_2:02d}/{month_2} - {day_1:02d}/{month_1}")
