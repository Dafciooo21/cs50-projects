text = input("Input: ").strip()
list = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]

print("Output: ", end="")
for _ in text:
    if _ not in list:
        print(_, end="")

print("", end="\n")
