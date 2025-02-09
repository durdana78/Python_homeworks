num = float((input("Insert the number: ")))
if int (num) == num: 
    print("last_digit:",int(num) % 10)

else: 
    list1 = str (num).split(".")
    print("last digit: ",list1[-1][-1])

    