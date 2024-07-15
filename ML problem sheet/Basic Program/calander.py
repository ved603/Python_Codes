import calendar

year = int(input("Enter the Year of calander you want : "))
month = int(input("Enter the Month : "))

if(month < 1 or month > 12):
    print("Please Provide the Valid Month")

print(calendar.month(year,month))