class Bank:
    def __init__(self):
        print("\nBank Portal successfully opened!\n")
    
    customer_accounts = {}

    def create_account(self, username, password):
        if username not in self.customer_accounts.keys():    
            self.customer_accounts[username] = [password, 0]
            print("\nAccount successfully created!\n")
        else:
            username = str(input("\nUsername already taken! Please try another username: "))
            self.create_account(username, password)

    def account_login(self, username, password):
        if len(self.customer_accounts) != 0:    
            if username in self.customer_accounts.keys():
                if self.customer_accounts[username][0] == password:
                    print("\nAccount successfully logged in!\n")
                    self.username = username
                    return -1
                else:
                    print("\nIncorrect password!\n")
                    return 0
            else:
                print("\nIncorrect username\n")
                return 0
        else:
            print("\nNo accounts created! Please create a account and try again!\n")
            return 0

    def deposit(self, deposit_amount):
        (self.customer_accounts[self.username])[1] += deposit_amount
        print("\nAmount successfully deposited! Transaction Completed!\n")

    def withdraw(self, withdraw_amount):
        if (self.customer_accounts[self.username])[1] >= withdraw_amount:
            (self.customer_accounts[self.username])[1] -= withdraw_amount
            print("\nAmount successfully withdrawn! Transaction Completed!\n")
        else:
            print(f"\nYou cannot withdraw more than your balance! Balance = {(self.customer_accounts[self.username])[1]}\n")

    def show_balance(self):
        print(f"\nYour account balance is ${(self.customer_accounts[self.username])[1]:.3f}\n")