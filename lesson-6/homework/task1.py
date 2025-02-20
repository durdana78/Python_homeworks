def check(func) :
    def wrapper(a,b) :
        if b == 0 :
            print("Denominator can't be zero")
            return
        func(a, b)
    return wrapper

@check
def div(a,b) :
    print(a / b)

div(6,0)
div(6,2)         
        