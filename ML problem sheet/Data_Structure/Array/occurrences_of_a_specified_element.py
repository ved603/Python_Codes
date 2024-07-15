list1 = [1,1,2,3,4,5,3,6,7,3,8,9]

num1 = int(input("Enter the Number to check occurences : "))
count = 0

for i in list1:
    if(i == num1):
        count += 1

print(f"The Number {num1} occured {count} times in the Array")
