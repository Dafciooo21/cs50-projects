coke_price = 50
accepted_coins = [5, 10, 25]
inserted = 0

while coke_price > inserted:
    coin = input("Insert Coin: ")
    if int(coin) in accepted_coins:
        inserted += int(coin)
    if inserted < 50:
        print("Amount Due:", coke_price - inserted)
    else:
        print("Change Owed:", -(coke_price - inserted))
