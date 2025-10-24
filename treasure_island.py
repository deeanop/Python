#Treasure Island game
score = 0
lives = 3
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
print("Welcome to Treasure Island!\n"
      "Your mission is to find the treasure.\n")
while score < 5 and lives > 0:
    first_step = input("You are at a cross road. Where do you want to go? Type 'left' or 'right'. ")
    if first_step == "left":
        score += 1
        second_step = input("You reached to a lake. What will you do now? Type 'swim' or 'wait'. ")
        if second_step == "wait":
            score += 2
            final_step = input("In front of you are three doors, each of them coloured different. Which one will you open? Type 'red', 'blue' or 'yellow'. ")
            if final_step == "blue":
                print("Eaten by beasts. You lost a life!")
                lives -= 1
            elif final_step == "red":
                print("Burned by fire. You loft a life!")
                lives -= 1
            elif final_step == "yellow":
                score += 3
                print("You won!")
                break
            else:
                print("You lost a life!")
                lives -= 1
        else:
            print("Attacked by trout. You lost a life!")
            lives -= 1
    else:
        print("Fall into a hole. You lost a life!")
        lives -= 1
if lives == 0:
    print("Game Over!")
else:
    print(f"Congratulations! You earned {score * 100} moneys!")

