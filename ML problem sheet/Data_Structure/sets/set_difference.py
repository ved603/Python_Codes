set1 = {6,5,3,1,2}
set2 = {5,6,4,7,8}

set3 = set2.difference(set1)

print("\nThe Set1 is  : ")
for i in set1:
    print(i ,  end = " ")

print("\n\nThe Set2 is  : ")
for i in set2:
    print(i ,  end = " ")

print("\n\nThe difference of set2 with set1 is : ")
for i in set3:
    print(i ,  end = " ")
print("\n")
