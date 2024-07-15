n = int(input("Enter the size of the Array : "))
array = []
for i in range(1,n+1):
    array_elements = int(input(f"Enter the {i} Array Element : "  ))
    array.append(array_elements)

for j in range(len(array)):
    print(f"{j+1} : " , array[j])
