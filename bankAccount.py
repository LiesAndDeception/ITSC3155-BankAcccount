# Author: Sophia Godfrey (TODO add Peter when merged in final branch)
# Class: Intro to Software Engineering (ITSC 3155)
# Date: February 13, 2025
# Assignment: Bank Account Part 2

import saving_account

class BankAccount:

    def __init__(self, name, curr_bal, mini_bal, account_number, routing_number):
        # Class Attribute: Title of the bank
        self.title = "Turbo Credit Union"

        # Instance Attributes
        self.name = name  # customer name
        self.curr_bal = curr_bal  # current balance
        self.mini_bal = mini_bal  # minimum balance

        self.__account_number = account_number  # Private member
        self._routing_number = routing_number  # Protected member

    # Method 1: deposit money
    def deposit(self, value):
        print(f"Current amount is {self.curr_bal}")
        
        if value > 0:
            self.curr_bal += value
            print(f"You deposited {value}. Your new balance is {self.curr_bal}.")
        else:
            print("You deposited an invalid amount")
 
    # Method 2: withdraw money
    def withdraw(self, value):
        print(f"Current amount is {self.curr_bal}")

        # Adding Validation: If remaining balance is less than minimal balance, user can't withdraw
        if value > 0 and self.curr_bal - value >= self.mini_bal:
            self.curr_bal -= value
            print(f"You withdrew {value}. Your new balance is {self.curr_bal}.")
        elif value > 0:
            print(f"Insufficient funds. Remaining balance must be at least {self.mini_bal}.")
        else:
            print("Withdrawal amount must be positive.")

    # Method 3: to get the account number safely
    def get_account_number(self):
        """Returns the masked account number (only last 4 digits visible)."""
        return f"****{str(self.__account_number)[-4:]}"

    # Method 4: to get the routing number (protected, but accessible)
    def get_routing_number(self):
        """Returns the routing number."""
        return self._routing_number

    # Method 5: print_customer_information (including the bank title)
    def print_customer_information(self):
        print(f"Account Information for {self.name} from {self.title}:")
        print(f"Current Balance: {self.curr_bal}")
        print(f"Minimum Balance: {self.mini_bal}")
        print(f"Account Number: {self.get_account_number()}")
        print(f"Routing Number: {self._routing_number}")  # Protected but accessible