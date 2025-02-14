# Author: Sophia Godfrey and Peter Crean
# Class: Intro to Software Engineering (ITSC 3155)
# Date: February 13, 2025
# Assignment: Bank Account Part 2

class BankAccount:

    def __init__(self, name, curr_bal, mini_bal, account_number, routing_number, daily_limit=0):
        # Class Attributes: Title of the bank, bank's routing number
        self.title = "Turbo Credit Union"

        # Instance Attributes
        self.name = name  # customer name
        self.curr_bal = curr_bal  # current balance
        self.mini_bal = mini_bal  # minimum balance
        self.__account_number = account_number  # Private member
        self._routing_number = routing_number  # Protected member
        self.daily_limit = daily_limit  # Maximum amount allowed per day

    # Error Checking Method
    def _validate_transaction(self, value, is_withdrawal=False):
        """Validates deposit and withdrawal transactions."""

        # Ensure the input is a valid number
        if not isinstance(value, (int, float)):
            print("Error: Invalid amount. Please enter a valid number.")
            return False

        # Ensure the transaction amount is positive
        if value <= 0:
            print("Error: Amount must be positive.")
            return False

        # Additional checks for withdrawals
        if is_withdrawal:
            if self.daily_limit - value < 0:
                print("Error: Unable to withdraw. Requested amount exceeds daily transfer limit.")
                return False
            if self.curr_bal - value < self.mini_bal:
                print("Error: Unable to withdraw. Requested amount exceeds available funds.")
                return False

        return True

    # Deposit method
    def deposit(self, value):
        """Deposit money after validation."""
        print(f"Current balance: ${self.curr_bal:.2f}")

        if self._validate_transaction(value):
            self.curr_bal += value
            print(f"Successfully deposited ${value:.2f}. New balance: ${self.curr_bal:.2f}.")
        else:
            print("Deposit failed.")

    # Withdraw method
    def withdraw(self, value):
        """Withdraw money after validation."""
        print(f"Current balance: ${self.curr_bal:.2f}, Daily limit: ${self.daily_limit:.2f}")

        if self._validate_transaction(value, is_withdrawal=True):
            self.curr_bal -= value
            self.daily_limit -= value
            print(
                f"Successfully withdrew ${value:.2f}. Remaining balance: ${self.curr_bal:.2f}. Daily limit left: ${self.daily_limit:.2f}.")
        else:
            print("Withdrawal failed.")

    # Method to get the account number safely
    def get_account_number(self):
        """Returns the masked account number (only last 4 digits visible)."""
        return f"****{str(self.__account_number)[-4:]}"

    # Method to get the routing number (protected, but accessible)
    def get_routing_number(self):
        """Returns the routing number."""
        return self._routing_number

    # Method to print the customer's information (including the bank title)
    def print_customer_information(self):
        print(f"Account Information for {self.name} from {self.title}:")
        print(f"Current Balance: {self.curr_bal}")
        print(f"Minimum Balance: {self.mini_bal}")
        print(f"Routing Number: {self._routing_number}")  # Protected but accessible

    def customer_action(self):
        print(f"What would you like to do?")
        context_action = input(f"deposit/withdraw/cancel: ")
        if context_action == "deposit":
            deposit_val = input(f"Please input the value you want to deposit: ")
            self.deposit(int(deposit_val))

        elif context_action == "withdraw":
            withdraw_val = input(f"Please input the value you want to withdraw: ")
            self.withdraw(int(withdraw_val))

        elif context_action == "cancel":
            pass

        else: print(f"Please try again.")




