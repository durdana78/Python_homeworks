sentence = input("Input sentence: ")
old_word = input("Replace: ")
new_word = input("With: ")

if old_word in sentence:
    print(sentence.replace(old_word,new_word))
else :
    print("The word wasn't found!")    