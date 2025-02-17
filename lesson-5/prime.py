import math
def is_prime(n) :
    for i in range(2,math.sqrt(n)) :
        if n % i == 0 :
            return False
        else :
            return True 