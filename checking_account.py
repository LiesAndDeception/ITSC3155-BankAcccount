from BankAccount import BankAccount

class CheckingAccount(BankAccount):

    def __init__(self, name, curr_bal, mini_bal, account_number, routing_number):
        super().__init__(name, curr_bal, mini_bal, account_number, routing_number)
        self.account_number = account_number
        self.mini_bal = mini_bal
        self.curr_bal = curr_bal
        self.bank_account = BankAccount(name, curr_bal, mini_bal, account_number, routing_number) # Create a BankAccount instance
        self.daily_limit = 10000 # Daily spending limit cap
