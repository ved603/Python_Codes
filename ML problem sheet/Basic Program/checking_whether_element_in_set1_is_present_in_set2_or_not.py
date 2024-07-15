color_list1 = set(["White","Black","Red"])
color_list2 = set(["Red","Green"])

for i in color_list1:
    if i not in color_list2:
        print(i , end=" ")