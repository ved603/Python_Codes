string = input("Enter the String : ")
if len(string) <= 3:
    print(string)
elif(string[-3:]== 'ing'):
    str1 = ""
    for i in range(0,len(string)-3):
        str1 += string[i]
    str1 += "ly"
    print(str1)
else:
    string += "ing"
    print(string)