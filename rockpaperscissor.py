#####################################################
"""Purpose : practicing coding with documentations """
"""Date: 04/02/2022"""
"""author: Sanchaitya"""
"""writing a code to play stone,paper, scissor with computer"""
#####################################################

# Adding the headers
# Return a random element from the non-empty sequence seq
import random


# Taking inputs for the game from the user and computer
# Rock paper scissors is a hand game for two or more players
def inputs_for_game():
    possible_reaction = ["rock", "paper", "scissor"]  # possible actions in the game
    computer_chose = random.choice(possible_reaction)  # taking random choices for computers from the actions
    human_chose = input("Please choose(rock, paper, scissor):  ")  # inputs for human actions
    print(f"\nYou chose {human_chose}, computer chose {computer_chose}.\n")
    return computer_chose, human_chose


#  The rules are straightforward: Rock smashes scissors, Paper covers rock, Scissors cut paper.
def who_the_winner(human_chose, computer_chose):
    if human_chose == computer_chose:
        print(f"Both players selected {human_chose}. It's a tie!")
    elif human_chose == "rock":
        if computer_chose == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif human_chose == "paper":
        if computer_chose == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif human_chose == "scissors":
        if computer_chose == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")


# The main function where other functions are called
if __name__ == "__main__":
    A, B = inputs_for_game()
    winner = who_the_winner(A, B)
