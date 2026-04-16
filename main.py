class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Pul qo'shildi:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Pul yechildi:", amount)
        else:
            print("Yetarli mablag' yo'q")

    def check_balance(self):
        print(self.owner, "balansi:", self.balance)


class ATM:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def show_accounts(self):
        for acc in self.accounts:
            acc.check_balance()


def main():
    a1 = Account("Ali", 500000)

    atm = ATM()

    atm.add_account(a1)

    a1.deposit(100000)
    a1.withdraw(200000)

    atm.show_accounts()


main()
