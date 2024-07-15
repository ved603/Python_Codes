str1 = "google.com"
str2 = ""
for i in str1:
    if i not in str2:
        str2 += i 
    else:
        str2 += '$'
print(str2)