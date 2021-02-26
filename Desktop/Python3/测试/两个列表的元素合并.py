list1 = [1,2,3,5]
list2 = [5,6,7]
list3 = [list1,list2]
print(list3)
list4 = []
list5 = []
for i in range(len(list3)):
    b = list3[i]
    list5 = list4 + b
    list4 = list5
print(list4) 

