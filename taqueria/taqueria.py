#menu - dictionary
menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

cost = 0

#infinite loop asking for input
while True:

    #if correct input add it to the sum
    try:
        item = input("Item: ").title().strip()

        if item in menu:
            cost = cost + float(menu[item])
            print(f"Total: ${cost:.2f}")

    #if incorrect input -> ignore and ask again
    except EOFError:
        break
    else:
        pass
