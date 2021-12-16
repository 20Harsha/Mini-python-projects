print("Welcome to Python Pizza Deliveries!")
user = input('Do you want to order pizza ? Y or N:')
if user == 'Y':
    print("\nMenu : ")
    print("Price of Small size pizza is $15, Medium size pizza is $20 ,Large size pizza is $25")
    print("Pepperoni for small size pizza is $2, Pepperoni for medium or large pizza is $3")
    print("Extra cheese would cost $1")
    size = input("\nChoose the size of pizza [ S ,M, L ] : ")
    add_pepperoni = input("Do you want pepperoni? Y or N : ")
    extra_cheese = input("Do you want extra cheese? Y or N : ")
    print('\nYour bill :')
    if size == "S":
        bill = 15
        print("Small size pizza : $15")
        if add_pepperoni == "Y":
            bill += 2
            print("Pepperoni is : $2")
    elif size == "M":
        bill = 20
        print("Medium size pizza : $15")
        if add_pepperoni == "Y":
            bill += 3
            print("Pepperoni is : $3")
    elif size == "L":
        bill = 25
        print("Medium size pizza : $25")
        if add_pepperoni == "Y":
            bill += 3
            print("Pepperoni is : $3")

    if extra_cheese == "Y":
        bill += 1
        print("extra cheese : $1")

    print(f"Total amount is : ${bill} ")
else:
    print('Ok! Thank You')