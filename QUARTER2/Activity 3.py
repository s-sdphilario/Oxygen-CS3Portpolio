class Bank_Account:
    def __init__(self, account_number, balance):
        self._account_number = account_number
        self._balance = balance
    @property
    def account_number(self):
        return self._account_number
    @property
    def balance(self):
        return self._balance
    @balance.setter
    def balance(self, new_balance):
        if new_balance >= 0:
            self._balance = new_balance
        else:
            print("Balance cannot be negative.")
            print(f"Current balance: {self._balance}")

account = Bank_Account(int(input("Enter your account number: ")), float(input("Enter your balance: ")))
print(f"Account Number: {account.account_number}")
print(f"Balance: {account.balance}")
account.balance = float(input("Enter new balance: "))