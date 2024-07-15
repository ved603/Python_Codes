set1 = {6,5,3,1,2}
set2 = {6,5,4,7,8}
print("\nThe Set1 is  : ")
for i in set1:
    print(i ,  end = " ")

print("\n\nThe Set2 is  : ")
for i in set2:
    print(i ,  end = " ")

set_intersection = set1.intersection(set2)
print("\n\nThe intersection of set is : ")
for i in set_intersection:
    print(i ,  end = " ")
print("\n")
