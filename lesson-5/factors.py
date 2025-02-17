num = int(input("enter the number: "))
for i in range(1,num + 1) :
    if num % i == 0 :
        print(f"{i} is a factor of {num}")