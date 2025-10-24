auction_dict = {}
maximum = 0
response = input("Are there other bids? yes/no")
while response != "no":
    name = input("Enter your name. ")
    money = int(input("How much money do you offer? "))
    auction_dict[name] = money
    for element in auction_dict.keys():
        if auction_dict[element] > maximum:
            maximum = auction_dict[element]
            person = element
    response = input("Are there other bids? yes/no")
print(f"The winner is {person}. The maximum price is {maximum}.")