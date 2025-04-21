from Bank import Bank

my_bank = Bank()
choice = -1
while choice != 0:
    choice = int(input("1.Create New Account\n2.Account Login\n0.Exit\n\nEnter your choice: "))
    
    if choice == 1:
        username = str(input("\nEnter your account username: "))
        password = str(input("Enter your account password: "))
        my_bank.create_account(username, password)
    
    elif choice == 2:
        username = str(input("\nEnter your account username: "))
        password = str(input("Enter your account password: "))
        inner_choice = my_bank.account_login(username, password)
        
        while inner_choice != 0:
            inner_choice = int(input("1.Deposit\n2.Withdraw\n3.Check Balance\n0.Exit\n\nEnter your choice: "))
            
            if inner_choice == 1:
                deposit_amount = float(input("Enter your deposit amount: "))
                while deposit_amount < 0:
                    deposit_amount = float(input("Please enter a positive value: "))
                my_bank.deposit(deposit_amount)
            
            elif inner_choice == 2:
                withdraw_amount = float(input("Enter your withdraw amount: "))
                while withdraw_amount < 0:
                    withdraw_amount = float(input("Please enter a positive value: "))
                my_bank.withdraw(withdraw_amount)
            
            elif inner_choice == 3:
                my_bank.show_balance()
                
            elif inner_choice == 0:
                print("\nLogging you out..\nSuccessfully logged out\n")

            else:
                print("\nPlease enter a valid number!\n")
    
    elif choice == 0:
        print("\nExiting the program...")
    
    else:
        print("\nPlease enter a valid number!\n")
exit(0)
