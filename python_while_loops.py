from datetime import date

# Create a date object for a specific date
specific_date = date(2024, 10, 30)  # Year, Month, Day

# Extract the month and day
month = specific_date.month
day = specific_date.day

print(f"Specific month: {month}")
print(f"Specific day: {day}")