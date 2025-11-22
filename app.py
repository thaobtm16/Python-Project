# print Welcome
print("Welcome to my Python program!")
# type in hours
hours = input("How many hours did you study today? ")
# calculate hours
hours = float(hours)
weekly_hours = hours * 7
# give solution
print(f"You are on track to study {weekly_hours} hours this week.")
# use for just in case
try:
    hours = float(hours)
except ValueError:
    print("Please enter a valid number.")
    exit()