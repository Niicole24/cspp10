bank_account = 10000
print("1. Withdraw \n2. Deposit \n3. Exit")
choice = input("Welcome to ATM! Pick from above [1|2|3]:")
while choice != "3":
    if choice == "1": #user chooses 'withdraw'
        amount = int(input("How much to withdraw: "))
        bank_account = bank_account - amount
    elif choice == "2":
        amount = int(input("How much to deposit: "))
        bank_account = bank_account + amount
    elif choice == "3": #user chooses 'exit'
        exit = input("Would you like to exit: ")
        

    print("1. Withdraw \n2. Deposit \n3. Exit")
    choice = input("Pick from above [1|2|3]:")                                                                                          