import calendar
import datetime

def calendar(month, year):
    cal = calendar.monthcalendar(year, month)
    print("{} {}".format(calendar.month_name[month], year))
    for week in cal:
        print(" ".join(str(day).rjust(2) for day in week))

# displays the current month and year
def current():
    now = datetime.datetime.now()
    calendar(now.month, now.year)

# displays a specific month and year
def specific_time():
    month = int(input("Enter the month (1-12): "))
    year = int(input("Enter the year (4-digit): "))
    calendar(month, year)

# Displays a menu to the user
while True:
    print("1. Display current month and year")
    print("2. Display specific month and year")
    print("3. Quit")
    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        current()
    elif choice == "2":
        specific_time()
    elif choice == "3":
        break