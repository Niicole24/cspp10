bank_account = 10000
print("1. Withdraw \n2. Deposit \n3. Exit")
choice = input("Welcome to ATM! Pick from above [1|2|3]:")
while choice != "3":
    if choice == "1": #user chooses 'withdraw'
        amount = input("How much do you wanna withdraw: ")
        bank_account = bank_account + amount
    elif choice == "2":
        amount = input("How much to deposit: ")
        bank_account = bank_account + amount
    elif choice == "3": #user chooses 'exit'
        exit = input("Would you like to exit: ")
        bank_account = bank_account + exit

    print("1. Withdraw \n2. Deposit \n3. Exit")
    choice = input("Pick from above [1|2|3]:")                                                                                          