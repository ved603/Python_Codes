list1 = [1,2,3,4,5]
print("The Original List is : " ,list1)
list2 = list1.copy() #directly Using list function we can copy/clone the List

print("The list is copied using Copy Function from list : " , list2)

#another way is

list3 = []
for i in list1:
    list3.append(i)

print("The List is Being copy by using for loop : " ,list3)