def prime(i):
    if i == 2 or i == 3 : 
        return True

    elif i % 2 == 0 or  i % 3 == 0:
        return False 
    else:
        j = 5
        while j * j <= i:
            if i % j == 0:
                return False
        j += 1
        return True



num = int(input('Enter the Number : '))
for i in range(2,num):
    if num % i == 0:
        if(prime(i)):
            print(i)
