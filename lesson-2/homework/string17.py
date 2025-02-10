text = input("Insert the string: ")
vowels = "aeoiu"
for char in text:
    if char in vowels:
        result = text.replace(char,"*")
print(result)        