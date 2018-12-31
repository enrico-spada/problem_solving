import re
import calendar

# Enter your code here. Read input from STDIN. Print output to STDOUT
month, day, year = map(lambda x : int((re.sub("^0", "", x))), input().split())

#Remember that print(int("08"))
#8

print(calendar.day_name[calendar.weekday(year, month, day)].upper())
