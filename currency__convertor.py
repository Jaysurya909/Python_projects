def convertor(amount,from_currency,to_currency):
    currencies={
        'USD':1.0,
        'INR':85.47,
        'EUR':0.85,
        'JPY':144.55,
        'CNY':7.16
    }

    usd_value=float(amount/currencies[from_currency])
    con_value=float(usd_value*currencies[to_currency])

    return round(con_value,2)# removes extra zero from float values


def display():
    print("Welcome to Currency Convertor\n")
    print("The Avaialble Currencies are\n1.USD\n2.INR\n3.EUR\n4.JPY\n5.CNY\n")

    try:
        from_currency=input("What is your currency (Please select the name from the options)\n").upper()
        amount=float(input("Enter the amount you want to convert\n"))
        to_currency=input("Which currency you want to convert your money into?(Please select the name from the options)\n").upper()
        conversion=convertor(amount,from_currency,to_currency) #Calling function in a function
        print(f"{amount} {from_currency} = {conversion} {to_currency}")
    except:
        print("You have entered invalid Value or Currency!!!\n")
    


display()