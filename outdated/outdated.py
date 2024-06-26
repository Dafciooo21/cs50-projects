# make a list with month
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

# when input with slashes it prints date in correct format
def dates_with_slashes(date):
    # if X/X/XXXX
    if len(date[0]) == 1 and len(date[1]) == 1 and int(date[0]) <=12 and int(date[1]) <= 31:
        print(f"{date[2]}-0{date[0]}-0{date[1]}")

    # if X/XX/XXXX
    elif len(date[0]) == 1 and len(date[1]) == 2 and int(date[0]) <=12 and int(date[1]) <= 31:
        print(f"{date[2]}-0{date[0]}-{date[1]}")

    # if XX/X/XXXX
    elif len(date[0]) == 2 and len(date[1]) == 1 and int(date[0]) <=12 and int(date[1]) <= 31:
        print(f"{date[2]}-{date[0]}-0{date[1]}")

    # if XX/XX/XXXX
    elif len(date[0]) == 2 and len(date[1]) == 2 and int(date[0]) <=12 and int(date[1]) <= 31:
        print(f"{date[2]}-{date[0]}-{date[1]}")

    elif date[0] > 12 or date[1] > 31:
        main()

def dates_with_month(date):
    new_date = date[0].split()

    if new_date[0] in months:
        index = months.index(new_date[0])

        if 10 <= (index + 1) <= 12 and int(new_date[1]) <= 31:
            if len(new_date[1]) == 2:
                print(f"{date[1].lstrip()}-{index + 1}-{new_date[1]}")

            elif len(new_date[1]) == 1:
                print(f"{date[1].lstrip()}-{index + 1}-0{new_date[1]}")

        elif (index + 1) <= 9 and int(new_date[1]) <= 31:
            if len(new_date[1]) == 2:
                print(f"{date[1].lstrip()}-0{index + 1}-{new_date[1]}")

            elif len(new_date[1]) == 1:
                print(f"{date[1].lstrip()}-0{index + 1}-0{new_date[1]}")
        elif int(new_date[1]) > 31:
            main()
    else:
        main()
def main():
    while True:
        date_str = input("Date: ")
        try:
            if len(date_str.split('/')) == 3:
                date = date_str.strip().split('/')
                dates_with_slashes(date)
                break

            if len(date_str.split(',')) == 2:
                date = date_str.split(',')
                dates_with_month(date)
                break

        except:
            pass


if __name__ == "__main__":
    main()
