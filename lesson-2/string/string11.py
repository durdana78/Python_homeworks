text = input("Enter a string: ")
if any(c.isdigit() for c in text):
    print("There is a digit")
else:
    print("There is not any digits")    