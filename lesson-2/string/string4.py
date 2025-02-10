text = input("Insert the string: ")
is_palyndrome = True
for i in range (len(text) // 2) :
    if text[i] != text[len(text) - 1 - i] :
        is_palyndrome = False
        break
if is_palyndrome:
    print("This is palyndrome")    
else :
    print("This is not palyndrome" )   