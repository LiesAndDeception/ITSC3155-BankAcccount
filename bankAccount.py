# Author: Sophia Godfrey (TODO add Peter when merged in final branch)
# Class: Intro to Software Engineering (ITSC 3155)
# Date: February 13, 2025
# Assignment: Bank Account Part 2

from savings_and_checking import SavingsAccount

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
        print(f"Account Information for {self.name} from {self.bank_title}:")
        print(f"Current Balance: {self.curr_bal}")
        print(f"Minimum Balance: {self.mini_bal}")

# Testing functions
# Prompt customer to input their information (customer name)
customer_name = input("Hello customer! If you have an account with us, enter your name: ")

# Create test accounts
customer1 = BankAccount(name="David", curr_bal=100.0, mini_bal=0.0)
customer2 = BankAccount(name="Ann", curr_bal=100.0, mini_bal=0.0)

# Match the entered name to the correct customer instance
if customer_name == customer1.name:
    customer_account = customer1
elif customer_name == customer2.name:
    customer_account = customer2
else:
    print("Invalid customer name. Please try again.")
    exit()  # Exit if customer is not found

# Greet the customer
print(f"Hello, {customer_name}! Welcome to {customer_account.title}.\n")

# Main interaction loop
while True:
    # Show options to the customer
    print("\nPlease choose an option:")
    print("1. View bank account info")
    print("2. Deposit money")
    print("3. Withdraw money")
    print("4. Exit")

    choice = input("Enter the number of your choice: ")

    if choice == "1":
        # Print account information
        customer_account.print_customer_information()

    elif choice == "2":
        # Deposit money
        try:
            deposit_amount = float(input("Enter the amount to deposit: "))
            customer_account.deposit(deposit_amount)
        except ValueError:
            print("Please enter a valid number.")

    elif choice == "3":
        # Withdraw money
        try:
            withdraw_amount = float(input("Enter the amount to withdraw: "))
            customer_account.withdraw(withdraw_amount)
        except ValueError:
            print("Please enter a valid number.")

    elif choice == "4":
        # Exit the loop and end the interaction
        print(f"Thank you for using {customer_account.title}. Have a great day!")
        break

    else:
        print("Invalid option. Please choose again.")




