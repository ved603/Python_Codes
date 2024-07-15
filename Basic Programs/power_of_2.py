num = int(input('Enter the number : '))
if(num < 31):
    for i in range(0,(2**num),2):
        print(i, end = " ")
else:
    print('The Number is greater than 2^31 so overflows')
