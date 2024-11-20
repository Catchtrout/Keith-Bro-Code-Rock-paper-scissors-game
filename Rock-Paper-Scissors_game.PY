import random

"""
Keith Frank
8th Period AP CSP - Mr. Mar
11/22/24
Rock, paper, scissors game
Bro Code:
https://www.youtube.com/watch?v=XKHEtdqhLK8&t=11148s
3:10:26 - 3:18:32
"""

while True:
    choices = ["rock", "paper", "scissors"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock, paper, or scissors?: ").lower()


    if player == computer:
        print("Computer: ", computer)
        print("Player", player)
        print("Tie!")
    
    elif player == "rock":
        if computer  == "paper":
            print("Computer: ", computer)
            print("Player", player)
            print("You lose!")
        if computer  == "scissors":
            print("Computer: ", computer)
            print("Player", player)
            print("You win!")
    elif player == "scissors":
        if computer  == "rock":
            print("Computer: ", computer)
            print("Player", player)
            print("You lose!")
        if computer  == "paper":
            print("Computer: ", computer)
            print("Player", player)
            print("You win!")
    elif player == "paper":
        if computer  == "scissors":
            print("Computer: ", computer)
            print("Player", player)
            print("You lose!")
        if computer  == "rock":
            print("Computer: ", computer)
            print("Player", player)
            print("You win!")
            
    play_again = input("Play again (yes/no): ").lower()
    
    if play_again != "yes":
        break
    
print("Bye!")
