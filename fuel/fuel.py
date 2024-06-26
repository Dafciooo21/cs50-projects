while True:
    userinput = input("Fraction: ")

    try:
        x, y = userinput.split("/")
        x = int(x)
        y = int(y)
        if x > y:
            continue
        result = ( x / y ) * 100
        result = round(result)

    except (ValueError, ZeroDivisionError):
        pass
    else:
        break

if result <= 1:
    print("E")
elif result >= 99:
    print("F")
else:
    print(f"{result}%")
