list1 = [1, 2, 3, 4,]
list2 = [1, 2, 2]
list11 = [x for x in list1 if x not in list2]
list22 = [x for x in list2 if x not in list1]
print(list11 + list22)