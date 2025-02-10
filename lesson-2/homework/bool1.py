username = input("Insert a username: ")
if username.strip() :
    password = input("Insert the password: ")
    if password.strip() :
        print("You have succesfully created a username and a password!")
    else :
        print("Password shouldn't be empty!") 
else :
    print("The username shouldn't be empty!")           