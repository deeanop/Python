#caesar cipher

from caesar_cipher_shift import codify
from caesar_cipher_logo import (print_logo, print_menu)

print_logo()
print("Welcome to the Caesar Cipher Simulator!\n")
print_menu()

cmd_number = int(input("Enter the command number. "))
while 0 < cmd_number < 6:
    if cmd_number == 1:
        print("You have selected Text Encoding.\n")
        message = input("Enter the message. ")
        key = int(input("Enter the key. "))
        enc = codify(message, key, "encode")
        print(f"The encoded version is {enc}.")
    elif cmd_number == 2:
        print("You have selected Text Decoding.\n")
        message = input("Enter the message. ")
        key = int(input("Enter the key ."))
        dec = codify(message, key, "decode")
        print(f"The decoded version is {dec}.")
    elif cmd_number == 3:
        print("You have selected File Encoding.\nEnter the message and key in the caesar_cipher_input.txt file.\n")
        with open("caesar_cipher_input.txt", "r") as fin:
            message = fin.readline()
            key = int(fin.readline())
        enc = codify(message, key, "encode")
        with open("caesar_cipher_output.txt", "w") as fout:
            fout.write(enc)
            fout.write("\n")
            fout.write(str(key))
    elif cmd_number == 4:
        print("You have selected File Decoding.\nEnter the message and key in the caesar_cipher_input.txt file.\n")
        with open("caesar_cipher_input.txt", "r") as fin:
            message = fin.readline()
            key = int(fin.readline())
        dec = codify(message, key, "decode")
        with open("caesar_cipher_output.txt", "w") as fout:
            fout.write(dec)
            fout.write("\n")
            fout.write(str(key))
    elif cmd_number == 5:
        print("You have selected Automatic Testing.\n")
        enc = input("Enter the encoded message. ")
        for key in range(1, 25):
            dec = codify(enc, key, "decode")
            print(dec)
    else:
        print("Unknown command.\n")
        exit()
    cmd_number = int(input("Enter the command number. "))









