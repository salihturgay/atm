#from operator import truediv
import random
print("\nRock, Paper, Scissors\n" )
user_score,computer_score=0,0
computer_options=["1","2","3"]
while True:
    print("\n - Rock\n - Paper\n - Scissors")
    user_choice= input("Your choice:")
    computer_choice= random.choice(computer_options)

    if user_choice=="1":
        if computer_choice=="1":
            print("Computer's choice: Rock\nRock equal to rock. Scoreless!")
        elif computer_choice=="2":
            print("Computer's choice: Paper\nPaper wraps stone. You lose!")
            computer_score +=100
        elif computer_choice=="3":
            print("Computer's choice: Scissors\nRock breaks scissors. You win!")
            user_score +=100
    elif user_choice=="2":
        if computer_choice=="1":
            print("Computer's choice: Rock\nPaper wraps stone. You win!")
            user_score +=100
        elif computer_choice=="2":
            print("Computer's choice: Paper\nPaper equal to Paper. Scoreless!")
        elif computer_choice=="3":
            print("Computer's choice: Scissors\nScissors cut Paper. You lose!")
            computer_score += 100
    elif user_choice=="3":
        if computer_choice=="1":
            print("Computer's choice: Rock\nRock breaks Scissors. You lose!")
            computer_score +=100
        elif computer_choice=="2":
            print("Computer's choice: Paper\nScissors cuts Paper. You win!")
            user_score +=100
        elif computer_choice=="3":
            print("Computer's choice: Scissors\nScissors equal to Scissors. Scoreless!")
    else:
        break
print("\n User's score:{}\n Computer's score:{}".format(user_score,computer_score))

if computer_score > user_score:
        print("Computer Win!")
elif computer_score < user_score:
        print("You win!\n Congrats")
elif computer_score==user_score:
        print("Scoreless")    
