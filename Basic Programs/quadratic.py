import math
a = int(input('Enter the Number 1  : '))
b = int(input('Enter the Number 2  : '))
c = int(input('Enter the number 3  : '))

print("The Quadratic Equation is : ",a,"x^2 + ",b,"x + ",c," = 0")

delta = b*b - 4*a*c
root1 = (-b + math.sqrt(delta)) //(2*a)
root2 = (-b - math.sqrt(delta)) //(2*a)

print("The First Root of the Equation is : ", root1)
print("The Second Root of the Equation is : ",root2)

