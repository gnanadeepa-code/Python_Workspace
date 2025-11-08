import random

def get_choices():
    player_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

def check_winner(player, computer):
    print(f"Player choice:{player} , Computer choice:{computer}")
    if player == computer:
        return "It's a tie!"
    elif player == "rock":
        if computer == "scissors":
            return "Rock crushes Scissors! You win!"
        else:
            return "Paper covers Rock! You lose!"
    elif player == "paper":
        if computer == "rock":
            return "Paper covers Rock! You win!"
        else:
            return "Scissors cut Paper! You lose!"
    elif player == "scissors":
        if computer == "paper":
            return "Scissors cut Paper! You win!"
        else:
            return "Rock crushes Scissors! You lose!"
   

def greeting():
    return "Welcome to Rock, Paper, Scissors!"

greet = greeting()
print(greet)

choices = get_choices()
result = check_winner(choices["player"], choices["computer"])
print("Result:", result)


