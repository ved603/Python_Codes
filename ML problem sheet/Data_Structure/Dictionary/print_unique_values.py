dic = {"IV" : "S001",
       "IX" : "S002",
       "VIII" : "S001",
       "VI" : "S005",
       "VII" : "S005",
       "V" : "S009",
       "VII" : "S007"}

list1 = []
for i in dic:

    if dic[i] not in list1:
        list1.append(dic[i])
for i in list1:
    print(i)