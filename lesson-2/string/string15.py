text = input("Insert the text here: ")
text_list = text.split()
list1 = "".join(word[0].upper() for word in text_list)
print(list1)