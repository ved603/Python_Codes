list1 = [1,2,3,1,4,5,1]
print("The List Before removing of Duplicates : " ,list1)
set1 = set(list1) #set operation will not accept the Duplicate element.so its easy to remove the duplicates
list2 = list(set1)
print("The List after removing Druplicates : " , list2)