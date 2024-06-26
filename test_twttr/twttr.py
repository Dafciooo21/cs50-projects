def main():
    text = input("Input: ").strip()
    output = shorten(text)
    print(f"Output: {output}")

def shorten(text):
    list = ["a", "e", "i", "o", "u"]
    print("Output: ", end="")
    shorten = []
    for _ in text:
        if _.casefold() not in list:
            shorten.append(_)
    output = str("".join(shorten))
    return output

if __name__ == "__main__":
    main()
