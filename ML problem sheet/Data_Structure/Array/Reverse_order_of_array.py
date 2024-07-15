list1 = [3,5,4,7]

print('The Array element before reverse order is : ' , list1)

for i in range(len(list1)//2):
    list1[i] , list1[len(list1)-(i+1)] = list1[len(list1)-(i+1)] , list1[i]

print("the array element in reverse order is : " , list1)  