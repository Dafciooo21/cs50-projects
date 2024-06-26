import inflect

x = inflect.engine()

names_list = []

try:
    while True:
        new_name = input("Name: ").capitalize().strip()
        names_list.append(new_name)

except EOFError:
    if len(names_list) >= 1:
        print("Adieu, adieu, to", x.join(names_list))
