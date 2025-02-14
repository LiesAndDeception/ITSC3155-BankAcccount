class SavingsAccount:
    """Savings account subclass with interest, compounding every year."""

    def __init__(self, name, account_number, balance=0.0, mini_bal=0.0, interest_rate=0.02, routing_number=None):
        from bankAccount import BankAccount  # Local import to avoid circular dependency
        self.bank_account = BankAccount(name, balance, mini_bal, account_number, routing_number)  # Create a BankAccount instance
        self.account_number = account_number
        self.interest_rate = interest_rate  # Annual interest rate (2%)

    def apply_interest(self, years=1):
        """Apply interest to the balance after 1 year."""
        self.bank_account.curr_bal *= (1 + self.interest_rate) ** years
        print(f"Interest applied. New balance after {years} year(s): ${self.bank_account.curr_bal:.2f}")

    def get_balance(self):
        return self.bank_account.curr_bal
