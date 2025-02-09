inserted_num = input("Insert 2 numbers:")
num_list = list(map(int,inserted_num.split()))
print("division:",int(num_list[0] / num_list[1]))
print("remainder:",int(num_list[0] % num_list[1]))