dic = {0:4,1:1,2:3,3:2};
print(dic)
list1 = list(dic.values())
print(list1)
list1.sort()
for i in range(len(dic)):
    dic[i] = list1[i]

print(dic)