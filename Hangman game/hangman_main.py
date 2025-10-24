#Hangman game

import random
from hangman_logo import print_message
from hangman_stages import (print_no_part_hang, print_head_hang, print_neck_hang,
                            print_first_hand_hang, print_second_hand_hang,
                            print_trunk_hang, print_first_leg_hang, print_second_leg_hang
                            )

word_list = ["abracadabra", "albania", "alphabet", "accident", "access", "accurate", "afghanistan", "ananas", "ancient", "apple", "application", "arctic", "assign", "assert",  "attic", "available", "badminton", "bag", "balcony", "baloon", "banana", "barcelona", "basketball", "bat", "battery", "bavaria", "beach", "bed", "beech", "beef", "bet", "bid", "bigger", "bil", "bipolar", "budapest", "bigfoot", "bucharest", "bachelor", "cabin", "cactus", "cabbage", "call", "calendar", "calory", "camouflage", "can", "canberra", "cape", "cappuccino", "caf", "carry", "cat", "category", "caviar", "car", "denmark", "dig", "dalmatia", "date", "dense", "deer", "debouncing", "deck", "dinosaur", "direction", "different", "diploma", "distortion", "dive", "dove", "dog", "door", "dome", "donkey", "dot", "dull", "dubious", "dublin", "duplicate", "edit", "edition", "elephant", "emphasize", "envelope", "erect", "essay"]
printed_characters = list()

print_message()
i = 0
index = random.randint(0, len(word_list) - 1)
word = word_list[index]

for j in range(0, len(word)):
    printed_characters.append("_")

while i <= 7 and "_" in printed_characters:
    print("".join(printed_characters))
    letter = input("Enter a letter. ").lower()
    if letter in word:
        print("Right!")
        for pos, char in enumerate(word):
            if char == letter:
                printed_characters[pos] = letter
    else:
        print("Wrong!")
        i += 1

    if i == 0:
        print_no_part_hang()
    elif i == 1:
        print_head_hang()
    elif i == 2:
        print_neck_hang()
    elif i == 3:
        print_first_hand_hang()
    elif i == 4:
        print_second_hand_hang()
    elif i == 5:
        print_trunk_hang()
    elif i == 6:
        print_first_leg_hang()
    elif i == 7:
        print_second_leg_hang()
        print("YOU LOSE!")
        print(f"The word was {word}.")
        exit()

print("YOU WIN!")
