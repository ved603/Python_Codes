num1 = int(input("Enter the Number to remove the First Occurence : "))
list1 = [1,1,2,3,4,5,3,6,7,3,8,9]
print("The List before the First Occurenced is : " ,list1)

for i in list1:
    if i == num1:
        list1.remove(i)
        break
print("The List after Removing of the First Occurenced of the Number is : " ,list1)