class CheckingAccount:

    def __init__(self, name, curr_bal, mini_bal):
        from BankAccount import BankAccount
        self.bank_account = BankAccount(name, curr_bal, mini_bal) # Create a BankAccount instance
        self.daily_limit = 10000 # Daily spending limit cap

    def withdraw(self, value):
        # If the value does not exceed the daily limit nor the current balance, withdraw the value.
        if self.daily_limit - value >= 0:
            if self.curr_bal - value < self.mini_bal:
                print('Unable to withdraw. Requested amount exceeds available funds.')
            else:
                self.curr_bal -= value
                self.daily_limit -= value
        else:
            print('Unable to withdraw. Requested amount exceeds daily transfer limit')