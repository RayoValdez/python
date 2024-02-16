#!/usr/bin/python3.10
while True:
    # Get choices from players
    player1 = input("Player 1, enter your choice (rock/paper/scissors): ").lower()
    player2 = input("Player 2, enter your choice (rock/paper/scissors): ").lower()

    # Check for a valid choice
    choices = ["rock", "paper", "scissors"]
    if player1 not in choices or player2 not in choices:
        print("Invalid choice. Please choose from rock, paper, or scissors.")
        continue

    # Determine the winner
    if player1 == player2:
        print("It's a tie!")
    elif (
        (player1 == "rock" and player2 == "scissors")
        or (player1 == "scissors" and player2 == "paper")
        or (player1 == "paper" and player2 == "rock")
    ):
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")

    # Ask if players want to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        break

