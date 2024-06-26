text = input("Expression: ").lower().strip()
x, y, z = text.split(" ")

if y == "+":
    print(float(x) + float(z))

elif y == "-":
    print(float(x) - float(z))

elif y == "*":
    print(float(x) * float(z))

elif y == "/":
    print(float(x) / float(z))
