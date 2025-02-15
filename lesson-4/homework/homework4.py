import random 
abc = True

while abc :
    tries = 0
    num = random.randint(1,100)
    while tries < 10 :
        guess = int(input("Guess the number: "))
        if guess < num:
            print("Too low!") 
            tries += 1   
        elif guess > num :
            print("Too high")
            tries += 1 
        else :
            print("Correct! Congrats")  
            tries = 0
            
    lost_question = input("You lost. Want to play again?")
    if lost_question != "YES" or "Y" or "y" or "yes" or "ok" :
        abc = False
    