def main():
    x = input("Greeting: ").lower().strip()
    print(f"${value(x)}")

def value(x):
    if x[0:5] == "hello":
        return 0
    elif x[0] == "h":
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
