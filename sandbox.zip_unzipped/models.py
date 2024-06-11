class Account:
    account_counter = 1000

    def __init__(self, name, email, address, account_type):
        self.account_number = Account.account_counter
        Account.account_counter += 1
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.balance = 0
        self.loan_amount = 0
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposited {amount}")
        return f"Deposited {amount}"

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdrew {amount}")
            return f"Withdrew {amount}"
        else:
            return "Insufficient balance"

    def check_balance(self):
        return self.balance

    def transaction_history(self):
        return self.transactions

    def take_loan(self, amount):
        self.loan_amount += amount
        self.transactions.append(f"Took loan {amount}")
        return f"Loan of {amount} approved"

    def transfer(self, amount, recipient):
        if amount <= self.balance:
            self.balance -= amount
            recipient.balance += amount
            self.transactions.append(
                f"Transferred {amount} to {recipient.account_number}"
            )
            recipient.transactions.append(
                f"Received {amount} from {self.account_number}"
            )
            return f"Transferred {amount} to account {recipient.account_number}"
        else:
            return "Insufficient balance"


class Bank:
    def __init__(self, name):
        self.name = name
        self.users = []
        self.loan_feature_active = True

    def create_account(self, name, email, address, account_type):
        new_account = Account(name, email, address, account_type)
        self.users.append(new_account)
        return new_account

    def delete_account(self, account_number):
        for user in self.users:
            if user.account_number == account_number:
                self.users.remove(user)
                return f"Account {account_number} deleted"
        return "Account not found"

    def get_all_accounts(self):
        return self.users

    def get_total_balance(self):
        return sum(user.balance for user in self.users)

    def get_total_loan_amount(self):
        return sum(user.loan_amount for user in self.users)

    def on_loan_feature(self):
        self.loan_feature_active = True
        return "Loan feature turned on"

    def off_loan_feature(self):
        self.loan_feature_active = False
        return "Loan feature turned off"


class Admin:
    def create_account(self, bank, name, email, address, account_type):
        return bank.create_account(name, email, address, account_type)

    def delete_account(self, bank, account_number):
        return bank.delete_account(account_number)

    def get_all_accounts(self, bank):
        return bank.get_all_accounts()

    def get_total_balance(self, bank):
        return bank.get_total_balance()

    def get_total_loan_amount(self, bank):
        return bank.get_total_loan_amount()
