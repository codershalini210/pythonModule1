balance = 1000  
def display_balance(bal):
    print(f"balance is ${bal}")
def deposite(bal,amount):
    if(amount<=0):
        print("deposite amt must be positive")
        return bal
    print("deposit done , curent balance ",bal+amount)
    return bal+amount
def withdraw(bal,amount):
    if(amount<=0):
        print("withdrawal must be a positive")
        return bal
    if(amount >bal):
        print("Insufficient Funds")
        return bal
    print("Withdrawal done , curent balance ",bal-amount)
    return bal-amount
while True:
    print("\n ATM") 
    print("1:check Balance")
    print("2. Deposite")
    print("3. Withdraw")
    print("4. exit")
    choice = input("choose an option (1-4)")
    if(choice=="1"):
        display_balance(balance)
    elif (choice =="2"):
        try:
            amount = float(input("enter deposite amount"))
            balance= deposite(balance,amount)
        except ValueError:
            print("invalid input please enter numeric value")
    elif (choice=="3"):
        try:
            amount = float(input("enter withdrawal amount"))
            balance= withdraw(balance,amount)
        except ValueError:
            print("invalid input please enter numeric value")
    elif(choice=="4"):
        print("Thank you for using ATM , bye")
        break
    else:
        print("invalid choice, press any no between 1-4")