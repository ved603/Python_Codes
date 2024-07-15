number = int(input('Enter the Number : '))
count = 0
res = 0
while(number != 0):
    a = number % 10
    number = number // 10
    count += 1
    res += a 
print("The Count of Numbers is : " , count)
print("The sum of the Number is : ", res)