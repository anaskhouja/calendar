import calendar
import datetime
import os
from API import Client

account_sid = "YOUR_ACCOUNT_SID"
auth_token = "YOUR_AUTH_TOKEN"
from_number = "YOUR_API_PHONE_NUMBER"
to_number = "THE_PHONE_NUMBER_TO_SEND_TO"
reminders = {}

def print_calendar(year, month):
    c = calendar.Calendar()
    month_days = c.itermonthdays(year, month)

    print("Su Mo Tu We Th Fr Sa")
    for week in month_days:
        for day in week:
            if day == 0:
                print("   ", end="")
            else:
                if (year, month, day) in reminders:
                    print("%2d*" % day, end="")
                else:
                    print("%2d " % day, end="")
        print()

def set_reminder(year, month, day, reminder):
    reminders[(year, month, day)] = reminder

def send_text_message(reminder):
    client = Client(account_sid, auth_token)
    client.messages.create(to=to_number, from_=from_number, body=reminder)

year = int(input("Enter the year: "))
month = int(input("Enter the month: "))

print_calendar(year, month)

while True:
    year = int(input("Enter the year for the reminder (0 to quit): "))
    if year == 0:
        break
    month = int(input("Enter the month for the reminder: "))
    day = int(input("Enter the day for the reminder: "))
    reminder = input("Enter the reminder: ")
    set_reminder(year, month, day, reminder)

while True:
    now = datetime.datetime.now()
    year = now.year
    month = now.month
    day = now.day

    if (year, month, day) in reminders:
        send_text_message(reminders[(year, month, day)])
    # Sleep
