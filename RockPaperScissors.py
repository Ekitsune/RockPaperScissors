# Rock Paper Scissors project
import random
player_decision = str(input("Would you like to play paper, rock or scissors? "))
player_decision = player_decision.lower()

if "paper" == player_decision:
  print("Player has " + player_decision + "!")
elif "rock" == player_decision:
  print("Player has " + player_decision + "!")
elif "scissors" == player_decision:
  print("Player has " + player_decision + "!")
else: 
  print("Please enter a valid value!") 
  quit()

computer_decision = ["paper", "rock", "scissors"] 
# using random.choice() to get a random value 
random_value = random.choice(computer_decision) 
# printing random value from list
print("Computer has " + random_value + "!") 

player_result = 0
computer_result = 0

while player_result == 3:
  print(player_result)
  
if player_decision == random_value:
    print("It is draw!")
if player_decision == "paper" and random_value == "rock":
    player_result += 1
    print("Player wins!")
if player_decision == "paper" and random_value == "scissors":
    computer_result += 1
    print("Computer wins!")
if player_decision == "rock" and random_value == "paper":
    computer_result += 1
    print("Computer wins!")
if player_decision == "rock" and random_value == "scissors":
    player_result += 1
    print("Player wins!")
if player_decision == "scissors" and random_value == "paper":
    player_result += 1
    print("Player wins!")
if player_decision == "scissors" and random_value == "rock":
    computer_result += 1
    print("Computer wins!")

if player_result >= 3:
  print("Player wins!!!")

if computer_result >= 3:
  print("Computer wins!!!")







