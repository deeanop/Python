#password random generator project

import random

big_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
small_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
special_symbols = ["+", "(", ")", "-", ".", ",", "*", "&", "^", "%", "$", "#", "@", "!", "?"]
password = list()

print("Welcome to Password Generator!\n")

number_of_big_letters = int(input("Enter the number of big letters. "))
number_of_small_letters = int(input("Enter the number of small letters. "))
number_of_digits = int(input("Enter the number of digits. "))
number_of_special_symbols = int(input("Enter the number of special symbols. "))

password_length = number_of_digits + number_of_special_symbols + number_of_small_letters + number_of_big_letters

i = 0
while i < password_length:
    character_type = random.randint(0, 3)
    if character_type == 0 and number_of_big_letters > 0:
        big_letter_index = random.randint(0, 25)
        password.append(big_letters[big_letter_index])
        number_of_big_letters -= 1
        i += 1
    elif character_type == 1 and number_of_small_letters > 0:
        small_letter_index = random.randint(0, 25)
        password.append(small_letters[small_letter_index])
        number_of_small_letters -= 1
        i += 1
    elif character_type == 2 and number_of_digits > 0:
        digit_index = random.randint(0, 9)
        password.append(digits[digit_index])
        number_of_digits -= 1
        i += 1
    elif character_type == 3 and number_of_special_symbols > 0:
        special_symbol_index = random.randint(0, 14)
        password.append(special_symbols[special_symbol_index])
        number_of_special_symbols -= 1
        i += 1
print("".join(password))