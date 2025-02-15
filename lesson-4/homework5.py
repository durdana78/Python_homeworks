password = input("Insert the password: ")

while len(password.strip()) < 8 and password.lower() == password :
    print("Characters shouldn't be less than 8 characters and must contain at least 1 Uppercse")
    password = input("Insert the password: ")
print("Password is strong.")