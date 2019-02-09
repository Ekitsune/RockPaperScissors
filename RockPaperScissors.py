# Rock Paper Scissors project
import random

player_result = 0
computer_result = 0

while (player_result == 3 or computer_result == 3) == False:
    player_decision = str(input("Would you like to play paper, rock or scissors? "))
    player_decision = player_decision.lower()

    if "paper" == player_decision:
        print("Player has " + player_decision + "!")
    elif "rock" == player_decision:
        print("Player has " + player_decision + "!")
    elif "scissors" == player_decision:
        print("Player has " + player_decision + "!")
    else: 
        print("Please enter a valid value! Valid values are 'paper', 'rock' or 'scissors'")
        quit()

    computer_decision = ["paper", "rock", "scissors"] 
    random_value = random.choice(computer_decision) 
    print("Computer has " + random_value + "!") 
    
    if player_decision == random_value:
        print("It is draw!")
    elif player_decision == "paper" and random_value == "rock":
        player_result += 1
        print("Player wins!")
    elif player_decision == "paper" and random_value == "scissors":
        computer_result += 1
        print("Computer wins!")
    elif player_decision == "rock" and random_value == "paper":
        computer_result += 1
        print("Computer wins!")
    elif player_decision == "rock" and random_value == "scissors":
        player_result += 1
        print("Player wins!")
    elif player_decision == "scissors" and random_value == "paper":
        player_result += 1
        print("Player wins!")
    elif player_decision == "scissors" and random_value == "rock":
        computer_result += 1
        print("Computer wins!")

if player_result == 3:
    print("Player is the winner! Congrats!")

elif computer_result == 3:
    print("Computer is the winner! Congrats!")





