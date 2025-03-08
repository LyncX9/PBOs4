class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrew ${amount}. New balance: ${self.balance}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def display_details(self):
        print(f"Account Number: {self.account_number}")
        print(f"Balance: ${self.balance}")


class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance=0, withdrawal_limit=500):
        super().__init__(account_number, balance)
        self.withdrawal_limit = withdrawal_limit

    def withdraw(self, amount):
        if amount > self.withdrawal_limit:
            print(f"Withdrawal failed. Amount exceeds the limit of ${self.withdrawal_limit}.")
        else:
            super().withdraw(amount)


class PremiumSavingsAccount(SavingsAccount):
    def __init__(self, account_number, balance=0, withdrawal_limit=2000):
        super().__init__(account_number, balance, withdrawal_limit)



if __name__ == "__main__":
    
    basic_account = BankAccount("123456789", 1000)
    basic_account.display_details()
    basic_account.deposit(500)
    basic_account.withdraw(200)
    basic_account.withdraw(1500) 
    print()

    
    savings_account = SavingsAccount("987654321", 1000)
    savings_account.display_details()
    savings_account.deposit(300)
    savings_account.withdraw(600) 
    savings_account.withdraw(400)
    print()

    
    premium_savings_account = PremiumSavingsAccount("567890123", 1000)
    premium_savings_account.display_details()
    premium_savings_account.deposit(1000)
    premium_savings_account.withdraw(2500)  
    premium_savings_account.withdraw(2000)