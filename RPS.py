
# Setting up player win counts
player_1_wins = 0
player_2_wins = 0

#Setting up while loop to run until someone gets 3 points
while player_1_wins < 3 and player_2_wins <3:
  player_1 = input("What is player 1 choice? rock, paper or scissors?\n").lower()
  # Setting up a pass to restart this loop if an invalid option is given
  if player_1 == "rock" or player_1 == "scissors" or player_1 == "paper":
        pass
  else:
    print("Invalid Option")
    continue
  player_2 = input("What is player 2 choice? rock, paper or scissors?\n").lower()
    # Setting up a pass to restart this loop if an invalid option is given

  if player_2 == "rock" or player_2 == "scissors" or player_2 == "paper":
    pass
  else:
    print("Invalid Option")
    continue

# Setting out game logic, and adding to player tallies
  if player_1 == "rock" and player_2 == "scissors":
    print("Player 1 wins")
    player_1_wins += 1
  elif player_1 == "rock" and player_2 == "paper":
    print("Player 2 wins")
    player_2_wins += 1
  elif player_1 == "rock" and player_2 == "rock":
    print("It's a tie")

  elif player_1 == "scissors" and player_2 == "paper":
    print("Player 1 wins")
    player_1_wins += 1
  elif player_1 == "scissors" and player_2 == "rock":
    print("Player 2 wins")
    player_2_wins += 1
  elif player_1 == "scissors" and player_2 == "scissors":
    print("It's a tie")

  elif player_1 == "paper" and player_2 == "rock":
    print("Player 1 wins")
    player_1_wins += 1
  elif player_1 == "paper" and player_2 == "scissors":
    print("Player 2 wins")
    player_2_wins += 1
  elif player_1 == "paper" and player_2 == "paper":
    print("It's a tie")

# Comparing points after while loop ends, displaying winner
if player_1_wins > player_2_wins:
  print(f"Player 1 wins with {player_1_wins} points to {player_2_wins}")

else:
  print(f"Player 2 wins with {player_2_wins} points to {player_1_wins}")