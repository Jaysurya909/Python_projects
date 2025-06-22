menu={ 
    'Vadapav':10,
    'Samosa':15,
    'Coffe':40,
    'Pizza':200,
    'Burger':150}

Total=0

print("Welcome to our Hotel Chads Kitchen")
print("The menu of this hotel is:\n 1.Vadapav: $10\n 2.Samosa: $15\n 3.Coffe: $40\n 4.Pizza: $200\n 5.Burger: $150")

Order_1=input("Enter the food you want to buy\t").capitalize()
if Order_1 in menu:
    Total += menu[Order_1]
else:
    print(f"The {Order_1} is not available in our menu!!")

while True:
    order_2=input("Do you want to add more items? (Yes/No)").capitalize()
    if (order_2=='Yes'):
        Order_1=input("Enter the food you want to buy\t").capitalize()
        if Order_1 in menu:
            Total += menu[Order_1]
        else:
            print(f"The {Order_1} is not available in our menu!!")
    elif(Total==0):
        print("You didnt order anything!!")
        break
    else:
        print("Your total order cost is $",Total)
        break




