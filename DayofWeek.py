""" Receives date in DD/MM/YYYY format
And prints the day in the week for that date"""

import calendar

date_input = input("Enter a date(DD/MM/YYYY): ")

if "/" in date_input:
    date_split = date_input.split('/')
elif "-" in date_input:
    date_split = date_input.split('-')
elif "." in date_input:
    date_split = date_input.split('.')
else:
    print("Invalid date format. Usage: DD/MM/YYYY")
    date_split = "ERROR: bad formatting"

date_calendar = calendar.day_name[calendar.weekday(
    int(date_split[2]), int(date_split[1]), int(date_split[0])
)]

print(f"For the date {date_input}, \nThe day of the week is {date_calendar}")
