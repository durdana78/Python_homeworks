nums_inserted = input("Insert 3 numbers: ")
nums_list = list(map(int,nums_inserted.split()))
print(max(nums_list))
print(min(nums_list))