def main():
    name = input("camelCase: ")
    print(snake_name(name))

def snake_name(name):
    snake = ""
    for i in name:
        if i.isupper():
            snake += "_" + i.lower()
        else:
            snake += i
    return snake.lstrip('_')

main()
