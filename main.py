

def deposit():
    while True:
        amount = input("What woulld you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("amount must be greater than 0.")
        else:
            print("Invalid input. Please enter a number.")
    return amount


