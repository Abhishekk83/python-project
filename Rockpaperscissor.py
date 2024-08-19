"""
Workflow of prooject
1-INput fom user(Rock, Paper, scissor)
2-Computer choice (computer will choose randomly not conditionally)
3- Result

Cases:
A- Rock
Rock - Rock =tie
Rock - Paper = Paper Win
Rock - scissor = Rock Win

B- paper
paper - Paper = tie
Paper - Rock = Paper
Paper - scissor = Scissor Win

C-scissor
scissor - scissor = tie
scissor - paper = scissor win
scissor - Rock = rock win"""

import random
item_list = ["Rock", "paper", "scissor"]

user_choice = input("Enter your move (Rock, Paper, scissor) = ")
comp_choice = random.choice(item_list)

print(f"user choice = {user_choice}")
print(f"Computer choice ={comp_choice}")
if user_choice == comp_choice:
    print("Both same : = Match Tie")

elif user_choice == "Rock":
    if comp_choice == "paper":
        print("paper capture rock = Computer win")
    else:
        print("Rock strick on scissor = You win")

elif user_choice == "paper":
    if comp_choice == "Rock":
        print("paper cover the rock =  you win")
    else:
        print("scissor cut the paper = computer win")

elif user_choice == "scissor":
    if comp_choice == "Rock":
        print("Rock breaks the scissor = computer win")
    else:
        print("scissor cut the paper = you win")

        