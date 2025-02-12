list1 = [1, 2, 3, 4, 5, 6,]
count = 0
length = len(list1)
for i in range(length) :
    if list1[i] % 2 == 1:
        count += 1
print(f"{count} numbers are even in the list")        