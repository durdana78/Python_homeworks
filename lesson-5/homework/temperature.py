def convert_cel_to_far(cel) :
    far = cel * 9 / 5 + 32
    return far
def convert_far_to_cel(far) :
    cel = (far - 32) * 5 / 9
    return cel
 
cel_input = int(input("Enter a temperature in C "))
cel_result = convert_cel_to_far(cel_input)
print(f"{cel_input} degrees C = {cel_result} degrees in F")

far_input = int(input("Enter a temperature in F "))
far_result = convert_far_to_cel(far_input)
print(f"{far_input} degrees F = {far_result: .2f} degrees in C")


