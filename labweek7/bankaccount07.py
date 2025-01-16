class BankAccount:
    Bank_accounts = 1
    def __init__(self, balance):
        self.balance = balance
        self.account_no = BankAccount.Bank_accounts
        BankAccount.Bank_accounts += 1

    def lodge(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def __str__(self):
        return f"Account number: {self.account_no}\nBalance: {self.balance}"

account1 = BankAccount(1000)
account2 = BankAccount(1500)

print(account1)
print(account2)

account1.lodge(500)
account2.withdraw(500)
print(account1)
print(account2)