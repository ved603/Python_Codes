set1 = {1,2,3,4}
print("\nThe Set before is  : ")
for i in set1:
    print(i ,  end = " ")
print("\n")
num = int(input("Enter the Number : "))
if num in set1:
    set1.remove(num)
    print("\n\nThe Set after the addion : ")
    for i in set1:
        print(i ,  end = " ")
    print("\n")
else:
    print("\n\n Element is not found in set")