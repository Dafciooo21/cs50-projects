import pyfiglet
import sys
import random

all_fonts = pyfiglet.FigletFont.getFonts()
x = random.choice(list(all_fonts))

def exit_program():
    sys.exit("Invalid usage")

try:
    if len(sys.argv) == 1:
        text = input("Input: ")
        text = pyfiglet.figlet_format(text, font = x)
        print(text)

    elif len(sys.argv) == 3 and sys.argv[2] in all_fonts and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
        text = input("Input: ")
        text = pyfiglet.figlet_format(text, font = sys.argv[2])
        print(text)

    else:
        exit_program()

except:
    exit_program()
