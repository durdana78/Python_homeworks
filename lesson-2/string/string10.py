text = input("Enter a sentence: ")
text_list = text.split()
print("The words in this sentence are: ")
for word in text_list:
    print(word,end = "\n")