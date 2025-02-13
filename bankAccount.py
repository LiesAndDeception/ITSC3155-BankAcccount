# Author: Sophia Godfrey (TODO add Peter when merged in final branch)
# Class: Intro to Software Engineering (ITSC 3155)
# Date: February 13, 2025
# Assignment: Bank Account Part 2

from savings_and_checking import SavingsAccount

class BankAccount:

        # Class Attribute: Title of the bank
        self.title = "Turbo Credit Union"

    # Instance Attributes: name (customer name), curr_bal (current balance), mini_bal (minimum balance)
    def __init__(self, name, curr_bal, mini_bal):

        self.name = name
        self.curr_bal = curr_bal
        self.mini_bal = mini_bal

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
        if value > 0 and self.curr_bal - amount >= self.mini_bal:
            self.curr_bal -= value
            print(f"You withdrew {value}. Your new balance is {self.curr_bal}.")
        elif amount > 0:
            print(f"Insufficient funds. Remaining balance must be at least {self.mini_bal}.")
        else:
            print("Withdrawal amount must be positive.")

    def print_customer_information(self):
        printstr = self.title + """ Account:
        --------------------------
        # Account Owner: """ + self.name + """
        Current Balance: """ + str(self.curr_bal)

        print(printstr)

        # Turbo Credit Union Account:
        # --------------------------
        # Account Owner: name
        # Current Balance: curr_bal



print("Testing the deposit function:")
acct1 = bankAccount('David', 100, 0)
acct2 = bankAccount('Ann', 100, 0)

acct1.print_customer_information()
acct1.deposit(200)
acct1.print_customer_information()

print("Testing the withdraw function:")
acct1.withdraw(100)
acct1.print_customer_information()
acct2.print_customer_information()
acct2.withdraw(200)
