def main():
    userinput = input("Fraction: ")
    percentage = convert(userinput)
    print(gauge(percentage))

def convert(userinput):
    while True:
        x, y = userinput.split("/")
        x = int(x)
        y = int(y)

        if x / y > 1:
            raise ValueError
        elif y == 0:
            raise ZeroDivisionError
        elif x > y:
            continue
        result = ( x / y ) * 100
        result = round(result)
        return int(result)



def gauge(result):
        try:
            if result <= 1:
                return "E"
            elif result >= 99:
                return "F"
            elif 1 < result < 99:
                return f"{int(result)}%"
            else:
                raise TypeError
        except TypeError:
            pass


if __name__ == "__main__":
    main()
