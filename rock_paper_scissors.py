#rock, paper, scissors game

import random

def print_rock():
    print('''
        _______  
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    ''')

def print_paper():
    print('''
        _______
    ---'   ____)____
              ______)
              ______)
             ______)
    ---._________)
    ''')

def print_scissors():
    print('''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    ''')

possibilities = ["rock", "paper", "scissors"]

index = random.randint(0, 2)
choice = int(input("Rock, Paper, Scissors..."))

while 0 <= choice <= 2:
    print("Computer's choice:\n")
    if possibilities[index] == "rock":
        print_rock()
    elif possibilities[index] == "paper":
        print_paper()
    else:
        print_scissors()

    print("Your choice:\n")
    if possibilities[choice] == "rock":
        print_rock()
    elif possibilities[choice] == "paper":
        print_paper()
    else:
        print_scissors()

    if possibilities[index] == "rock":
        if possibilities[choice] == "rock":
            print("It's a draw!")
        elif possibilities[choice] == "paper":
            print("You win!")
        else:
            print("You lose!")
    elif possibilities[index] == "paper":
        if possibilities[choice] == "rock":
            print("You lose!")
        elif possibilities[choice] == "paper":
            print("It's a draw!")
        else:
            print("You win!")
    else:
        if possibilities[choice] == "rock":
            print("You win!")
        elif possibilities[choice] == "paper":
            print("You lose!")
        else:
            print("It's a draw!")
    choice = int(input("Rock, Paper, Scissors..."))
