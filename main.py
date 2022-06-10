import random
randomNum = random.randint(0, 2)

choices = ["rock", "paper", "scissor"]

UserChoices = input("inter your choice:")

pcChoice = choices[randomNum]


if UserChoices == "rock" or UserChoices == "paper" or UserChoices == "scissor":
    print(f"PC Choice {pcChoice}")
    if pcChoice == UserChoices:
        print("it's a tie!")
    else:
        if pcChoice == "rock":
            if UserChoices == "paper":
                print("you win!")
            else:
                ("You lost!")
        if pcChoice == "paper":
            if UserChoices == "scissor":
                print("you win!")
            else:
                print("You lost!")
        if pcChoice == "scissor":
            if UserChoices == "rock":
                print("you win!")
            else:
                print("You lost!")
else:
    print("Wrong choice!")

#---------------Reza_sdo-------------------