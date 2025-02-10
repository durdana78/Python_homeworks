text = input("Insert the word: ").lower()
vowels = "aeoui"
vowel_count = 0
consonant_count = 0
for char in text:
    if char in vowels:
        vowel_count += 1
    else :
        consonant_count += 1
print("The number of vowels:", vowel_count) 
print("The number of consonants:",consonant_count)           