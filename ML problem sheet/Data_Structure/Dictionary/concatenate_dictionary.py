dic = {}
office_colleague = {1:'Tushar',2:'Vaibhav'}
Roommate = {1:'Vishal',2:'Tejas',3:'Aakash',4:'Gunvant',5:'Sarthak'}

print("\n The First Subdict is : " , office_colleague)
print("\n The Second Subdict is :" , Roommate)
print("\n The Concatenated Dict before Operation is : ",dic)
list1 = list(office_colleague.values()) + list(Roommate.values())

for i in range(len(list1)):
    dic[i+1] = list1[i]

print("\n The Concatenated Dict after Operation is : ",dic)
print()