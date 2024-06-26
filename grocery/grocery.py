#make an empty dictionary
grocery = {}
#infinite loop
while True:
    try:
        #create a list
        product = input().strip().upper()
        if product in grocery:
            grocery[product] += 1
        else:
            grocery[product] = 1
    except EOFError:
        #loop for counting number of occurence
        #and printing without any duplicate
        for key in sorted(grocery.keys()):
            print(grocery[key], key)

        break
