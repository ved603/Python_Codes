year = int(input('Enter the year : '))
if (year%4 == 0) and ((year%400 == 0) or(year % 100 != 0)):
    print('The Given Year is an Leap Year')
else:
    print("It is Not an Leap Year")