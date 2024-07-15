array = []

m = int(input("Enter the Number of Rows : "))
n = int(input("Enter the Number of Columns : "))

for i in range(m):
    sub_array = []
    for j in range(n):
        a = int(input("Enter the Location : "))
        sub_array.append(a)
    array.append(sub_array)

print("The Array Elements is : ")
for k in range(m):
    for l in range(n):
        print(array[k][l], end = " ")
    print()