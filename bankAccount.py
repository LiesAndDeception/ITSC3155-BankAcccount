# Author: Sophia Godfrey (TODO add Peter when merged in final branch)
# Class: Intro to Software Engineering (ITSC 3155)
# Date: February 13, 2025
# Assignment: Bank Account Part 2

from savings_account import SavingsAccount

class BankAccount:

    def __init__(self, name, curr_bal, mini_bal):
        # Class Attribute: Title of the bank
        self.title = "Turbo Credit Union"

        # Instance Attributes
        self.name = name  # customer name
        self.curr_bal = curr_bal  # current balance
        self.mini_bal = mini_bal  # minimum balance

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

    # Method 3: print_customer_information (including the bank title)
    def print_customer_information(self):
        print(f"Account Information for {self.name} from {self.title}:")
        print(f"Current Balance: {self.curr_bal}")
        print(f"Minimum Balance: {self.mini_bal}")




