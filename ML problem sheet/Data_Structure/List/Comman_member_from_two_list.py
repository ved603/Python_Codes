list1 = [1,2,3,4,5]
list2 = [5,6,7,8,9]

count = 0
for i in list1:
    if i in list2:
        print(True)
    else:
        count += 1

if(count == len(list1)):
    print(False);