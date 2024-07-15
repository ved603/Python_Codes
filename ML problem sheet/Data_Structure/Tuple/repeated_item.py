tuple1 = (1,2,3,1,4,5,1,4)
list1 = []
for i in range(len(tuple1)):
    count = 1
    for j in range(i+1,len(tuple1)):
        if tuple1[i] == tuple1[j]:
            count += 1
    if(count > 1 and tuple1[i] not in list1):
        list1.append(tuple1[i])
print("The Element list which are repeated in the tuple is : ",list1)