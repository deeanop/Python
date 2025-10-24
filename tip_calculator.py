# tip calculator
price = round(float(input("Enter the price of the bill. ")), 2)
persons = int(input("How many people did split the bill? "))
amount = round(float(input("How much tip would you like to give? ")))
percent = amount / 100
result = round(price / persons * (1 + percent), 2)
print(f"Everyone must pay {result}")









