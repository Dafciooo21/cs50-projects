def main():
    s = input("Plate: ")
    if is_valid(s):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # Count the number of digits in the string
    digit_count = 0
    # Check the length of the string
    if(len(s) < 2 or len(s) > 6 ):
        return False
    # Makes sure the first two characters are not numbers
    if(s[0].isdigit() or s[1].isdigit()):
        return False
    for char in s:
        # Make sure only valid characters are in the string, no special characters or spaces
        if( not char.isalnum()):
            return False
        # Check to see if digits are in the middle of the string
        if(digit_count > 1 and char.isalpha()):
            return False
        # Count for the number of digits in the string
        if(char.isdigit()):
            digit_count += 1
        # Make certain the first instance of the digit is not 0
        if(digit_count == 1 and char == "0"):
            return False
    # final return
    return True

if __name__ == "__main__":
    main()
