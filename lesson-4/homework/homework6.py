from math import sqrt


for i in range(2,101) :
    for j in range(2,int(sqrt(i)) + 1) :
        if i % j == 0 :
            continue
        else :
            print(i)