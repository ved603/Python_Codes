string = "Learning"
dic = {}
for i in range(len(string)):
    if string[i] in dic:
        dic[string[i]] += 1
    else:
        dic[string[i]] = 1

for i in dic:
    print(f"{i} = {dic[i]}")
