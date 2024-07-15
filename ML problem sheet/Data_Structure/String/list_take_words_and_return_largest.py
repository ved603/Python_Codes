print("Enter the String : ",end = " ")
list1 = list(map(str,input().split(" ")))
flag = 0
max_length = len(list1[0])
flag = list1[0]
for i in list1:
    if(len(i) > max_length):
        max_length = len(i)
        flag = i
print(f"The String is '{flag}' with the Maximum length of '{max_length}'")