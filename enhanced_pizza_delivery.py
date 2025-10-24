#if/elif/else/for/array project, without functions
import time

my_money = float(input("Me: How much money do I have?"))
total_time = 0

print("Waiter: Welcome to our Pizza Delivery Service!\n")
print("Here is your menu.\n\n"
      "              Sizes:\n"
      "ExtraLarge----------------------20$\n"
      "Large---------------------------15$\n"
      "Medium--------------------------10$\n"
      "Small----------------------------5$\n\n"
      "Tomato Sauce---------------------5$\n\n"
      "Cheese\n\n"
      "Mozarella-----------------------10$\n"
      "Parmesan------------------------40$\n"
      "Ricotta-------------------------25$\n"
      "Gorgonzola----------------------30$\n"
      "Feta----------------------------20$\n\n"
      "Veggies\n\n"
      "Peppers-------------------------10$\n"
      "Tomatoes-------------------------5$\n"
      "Mushrooms-----------------------15$\n"
      "Aubergines----------------------20$\n"
      "Cucumbers------------------------7$\n"
      "Pineapples----------------------25$\n"
      "Onions--------------------------10$\n"
      "Olives---------------------------4$\n\n"
      "Meat\n\n"
      "Salami--------------------------10$\n"
      "Ham-----------------------------14$\n"
      "Chicken-------------------------21$\n"
      "Beef----------------------------40$\n"
      "Sausages------------------------32$\n"
      "Tuna----------------------------28$\n"
      "Bacon---------------------------20$\n"
      "Extra Sauces\n\n"
      "Ketchup--------------------------5$\n"
      "Cheese----------------------------8$\n"
      "Garlic---------------------------7$\n"
      "Barbeque------------------------10$\n"
      "Tzatziki-------------------------8$\n"
      "Chili---------------------------10$\n\n"
      "To Go----------------------------\n\n"
      "        ~~~Bon Appetit!~~~\n\n")

price = 0

size = input("Waiter: What size of pizza do you want? ExtraLarge(el), Large(l), Medium(m), Small(s)")
print(f"Me: {size}.")
if size == "el":
    price += 20
    total_time += 20
elif size == "l":
    price += 15
    total_time += 15
elif size == "m":
    price += 10
    total_time += 10
elif size == "s":
    price += 5
    total_time += 5

souce_preferency = input("Waiter: Do you want sauce? Yes(y), No(n)")
print(f"Me: {souce_preferency}.")
if souce_preferency == "y":
    price += 5
    total_time += 5
else:
    pass

cheese_prefferencies = []
cheese = input("Waiter: Do you want cheese on pizza? What type of cheese?").capitalize()
print(f"Me: {cheese}.")
while cheese != "No more":
    cheese_prefferencies.append(cheese)
    cheese = input("Waiter: One more type?").capitalize()
    print(f"Me: {cheese}.")
for i in cheese_prefferencies:
    if i == "Mozarella":
        price += 10
        total_time += 5
    elif i == "Parmesan":
        price += 40
        total_time += 10
    elif i == "Ricotta":
        price += 25
        total_time += 5
    elif i == "Gorgonzola":
        price += 30
        total_time += 10
    elif i == "Feta":
        price += 20
        total_time += 5

veggies_prefferencies = []
veggie = input("Waiter: Do you want weggies on pizza? What type of weggie?").capitalize()
print(f"Me: {veggie}.")
while veggie != "No more":
    veggies_prefferencies.append(veggie)
    veggie = input("Waiter: One more type?").capitalize()
    print(f"Me: {veggie}.")
for i in veggies_prefferencies:
    if i == "Peppers":
        price += 10
        total_time += 10
    elif i == "Tomatoes":
        price += 5
        total_time += 5
    elif i == "Mushrooms":
        price += 15
        total_time += 5
    elif i == "Aubergines":
        price += 20
        total_time += 15
    elif i == "Cucumbers":
        price += 7
        total_time += 20
    elif i == "Pineapples":
        price += 25
        total_time += 10
    elif i == "Onions":
        price += 10
        total_time += 10
    elif i == "Olives":
        price += 4
        total_time += 5

meat_prefferencies = []
meat = input("Waiter: Do you want meat on pizza? What type of meat?").capitalize()
print(f"Me: {meat}.")
while meat != "No more":
    meat_prefferencies.append(meat)
    meat = input("Waiter: One more type?").capitalize()
    print(f"Me: {meat}.")
for i in meat_prefferencies:
    if i == "Salami":
        price += 10
        total_time += 15
    elif i == "Ham":
        price += 14
        total_time += 15
    elif i == "Bacon":
        price += 20
        total_time += 20
    elif i == "Sausages":
        price += 32
        total_time += 25
    elif i == "Chicken":
        price += 21
        total_time += 25
    elif i == "Beef":
        price += 40
        total_time += 35
    elif i == "Tuna":
        price += 28
        total_time += 30

sauce_prefferencies = list()
sauce = input("Waiter: Do you want extra sauces on pizza? What type of sauce?").capitalize()
print(f"Me: {sauce}.")
while sauce != "No more":
    sauce_prefferencies.append(sauce)
    sauce = input("Waiter: One more type?").capitalize()
    print(f"Me: {sauce}.")
for i in sauce_prefferencies:
    if i == "Ketchup":
        price += 5
        total_time += 3
    elif i == "Garlic":
        price += 7
        total_time += 10
    elif i == "Barbeque":
        price += 10
        total_time += 3
    elif i == "Cheese":
        price += 8
        total_time += 3
    elif i == "Tzatziki":
        price += 8
        total_time += 10
    elif i == "Chili":
        price += 10
        total_time += 10

place = input("Waiter: Do you serve here or to go? Here(h), ToGo(t)")
print(f"Me: {place}.")
if place == "t":
    price += 10

print(f"Waiter: Your pizza will be done in {time} minutes.")

time.sleep(total_time)

print("Waiter: Here is your pizza!")
print("Me: Thank you!")
tips = float(input("Me: May I give some tips?"))
print(tips)
print("\n")
if tips > 0:
    print(f"Waiter: Thank yow very much!")
else:
    pass

time.sleep(20)

print("Me: I want to pay!")
time.sleep(5)
print("Waiter: Sure, here is your bill!\n\n"
      "~~~Payment Receipt~~~\n"
      "")











