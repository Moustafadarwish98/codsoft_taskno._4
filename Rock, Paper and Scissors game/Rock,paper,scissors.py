"""Importing required library for the game"""
import random


"""From Ascii Art getting the required shapes."""
rock = """ Rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """ Paper
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """ Scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

options_list = [rock, scissors, paper]
your_score = 0
computer_score = 0

still_playing = True
print("-----------------Welcome to Rock,Paper,Scissors Game.---------------------\n")
print("---------------Rules---------------")
print("Rules are simple rock beats scissors, scissors beats paper and paper beats rock.")
print("---------------Start---------------")
start = input("Are you ready to start playing? (yes/no) ").lower()
if start == "yes":
    while still_playing:
        valid_choice = False

        while not valid_choice:
            user_choice = int(input("Choose rock (type 0), scissors (type 1) or paper (type 2): "))
            if user_choice < 3:
                valid_choice = True

        computer_choice = random.randint(0, 2)

        print(f"You choose: {options_list[user_choice]}")
        print(f"Computer chose: {options_list[computer_choice]}")

        if user_choice == 2 and computer_choice == 0:
            your_score += 1
            print(f"You win 🥳!.\n Scores: {your_score}/{computer_score}")
        elif user_choice == 0 and computer_choice == 2:
            computer_score += 1
            print(f"You lose 😢.\n Scores: {your_score}/{computer_score}")
        elif user_choice < computer_choice:
            your_score += 1
            print(f"You win 🥳!.\n Scores: {your_score}/{computer_score}")
        elif user_choice == computer_choice:
            print("Draw.")
            print(f"Scores: {your_score}/{computer_score}")
        else:
            computer_score += 1
            print(f"You lose 😢.\n Scores: {your_score}/{computer_score}")

        play_again = input("Do you want to play again? (Yes/No) ").lower()
        if play_again == "no":
            still_playing = False
            print(f"Final Score: {your_score}/{computer_score}")
            if your_score > computer_score:
                print("You won 🥳!")
            else:
                print("You lost 😢")
else:
    print("Come when you are ready.")







