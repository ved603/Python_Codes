t = int(input('Enter the Tempreture in Fahrenheit : '))
v = int(input('Enter the Speed of the Wind (in miles/hour) : '))

if(t > 50) or (v> 120 or v < 3):
    w = 35.74 + (0.6215 * t) + ((0.4275 * t) - 35.75) * (v**0.16)

else:
    print("there was error in the value of Tempreture or Speed of wind")

''' The formula is not valid if t is larger than 50 in absolute value or if v is larger
    than 120 or less than 3 '''

print("The Effective tempreture would be : ",w)