import random
while True :
    comp_score = 0
    user_score = 0

    game = ["rock", "paper", "scissors"]
    while comp_score < 5 or user_score < 5:
        comp = random.choice(game)
        abc = True

        while abc :
            user_input = input("Enter your choice(1.scissors, 2.rock, 3.paper): ")
            if user_input == "1" :
                user = "scissors"
                abc = False
            elif user_input == "2" :
                user = "rock"
                abc = False
            elif user_input == "3" "" :
                user = "paper"
                abc = False    
            else :
                print("Please insert available choice: ")       

        
        if comp == "rock" and user == "scissors" :
            comp_score += 1
            print(f"Comp wins!\n Comp: {comp_score}, User: {user_score}" )
        elif comp == "rock" and user == "paper" :
            user_score += 1
            print(f"User wins!\n Comp: {comp_score}, User: {user_score}" )   
        elif comp == "paper" and user == "scissors" :
            user_score += 1
            print(f"User wins!\n Comp: {comp_score}, User: {user_score}" )     
        elif comp == "paper" and user == "rock" :
            comp_score += 1
            print(f"Comp wins!\n Comp: {comp_score}, User: {user_score}" )   
        elif comp == "scissors" and user == "paper" :
            comp_score += 1
            print(f"Comp wins!\n Comp: {comp_score}, User: {user_score}" )    
        elif comp == "scissors" and user == "stone" :
            user_score += 1
            print(f"Comp wins!\n Comp: {comp_score}, User: {user_score}" )  
        else :
            print("Draw!")
            print(f" Comp: {comp_score}, User: {user_score}" )

    if comp_score == 5 :
        print("Comp wins!")
    else :
        print("User wins!")    