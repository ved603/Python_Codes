tuple1 = (1,2,3,4,5,6)
print("\nThe Original Tuple is : ",tuple1)
# Tuple is unchangable so we cannot remove the item directly 

list1 = list(tuple1)
list1.remove(6)
tuple2 = tuple(list1)
print("The Updated tuple is : " ,tuple2)
print()