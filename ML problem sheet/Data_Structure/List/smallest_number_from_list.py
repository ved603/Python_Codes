l1 = [4,7,6,3,5]

smallest = l1[0]
print("\nThe List elements are : ")
for i in l1:
    if i < smallest:
        smallest = i
    print(i , end =" ")

print("\n\nThe smallest of the All element in the list is : " ,smallest)
print("\n")