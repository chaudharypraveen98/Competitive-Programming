import calendar

date = list(map(int, input().split()))
day = calendar.weekday(date[2], date[0], date[1])
print(calendar.day_name[day].upper())

