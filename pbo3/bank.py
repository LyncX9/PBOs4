class BankAccount:
    def __init__(self, account_holder, balance, pin):
        self.account_holder = account_holder  
        self._balance = balance  
        self.__pin = pin  

    def get_balance(self):
        return self._balance

    def set_balance(self, amount):
        if amount > 0:
            self._balance = amount
            print(f"Balance updated successfully. New balance: ${self._balance}")
        else:
            print("Invalid balance amount. Balance must be positive.")

    def verify_pin(self, pin):
        return self.__pin == pin

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited ${amount}. New balance: ${self._balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self._balance}")
        else:
            print("Insufficient funds or invalid amount.")

    def get_account_holder(self):
        return self.account_holder

def bank_account_menu():
    account = BankAccount("Bagas Firmansyah", 1500, "1234")
    
    
    while True:
        entered_pin = input("Enter PIN to access account: ")
        if account.verify_pin(entered_pin):
            print("PIN verification successful. Access granted.")
            break
        else:
            print("Incorrect PIN. Please try again.")
    
    while True:
        print("\nBank Account Menu:")
        print(f"Account Holder: {account.get_account_holder()}")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif choice == "2":
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif choice == "3":
            print(f"Current Balance: ${account.get_balance()}")
        elif choice == "4":
            print("Exiting Bank Account System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

bank_account_menu()