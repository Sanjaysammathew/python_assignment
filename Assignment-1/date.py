from datetime import date, datetime, timedelta

# 1. date.today()
today = date.today()
print("1. Today's date:", today)


# 2. datetime.now()
current_datetime = datetime.now()
print("2. Current date and time:", current_datetime)


# 3. .year
print("3. Year:", today.year)


# 4. .month
print("4. Month:", today.month)


# 5. .day
print("5. Day:", today.day)


# 6. .strftime()
formatted_date = today.strftime("%d-%m-%Y")
print("6. Formatted date:", formatted_date)


# 7. .strptime()
date_string = "24-09-2026"
converted_date = datetime.strptime(date_string, "%d-%m-%Y")
print("7. Converted string to date:", converted_date)


# 8. timedelta()
future_date = today + timedelta(days=5)
print("8. Date after 5 days:", future_date)


# 9. .weekday()
weekday_number = today.weekday()
print("9. Weekday number:", weekday_number)


# 10. .date()
only_date = current_datetime.date()
print("10. Date from datetime:", only_date)