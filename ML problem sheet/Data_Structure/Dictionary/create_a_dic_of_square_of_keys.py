dic = {}
print()
num = int(input("Enter the Number for which you want to create a dictionary : "))
for i in range(1,num+1):
    dic[i] = i*i

print("\nThe dictionary of the square of the keys is : " )

for i in dic:
    print(f"{i} = {dic.get(i)}")