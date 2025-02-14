# Author: Sophia Godfrey and Peter Crean
# Class: Intro to Software Engineering (ITSC 3155)
# Date: February 13, 2025
# Assignment: Bank Account Part 2



# Test Cases For Assignment:

# Checking Account:
# Case 1:
    # Run file
    # type "David"
    # type "2"
    # type "deposit"
    # type "2000"
    # type "4"

# Case 2:

    # Run file
    # type "Ann"
    # type "2"
    # type "withdraw"
    # type "11000"
    # type "4"

# Savings Account:
# Case 1:
    # Run file
    # type "David"
    # type "3"
    # type "withdraw"
    # type "2000"
    # type "4"

# Case 2:

    # Run file
    # type "Ann"
    # type "3"
    # type "cancel"
    # type "4"



import checking_account
from bankAccount import BankAccount
from checking_account import CheckingAccount
from saving_account import SavingsAccount

# Testing functions
# Prompt customer to input their information (customer name)
customer_name = input("Hello customer! If you have an account with us, enter your name: ")

# Create test accounts
# Routing number is the same as there is only one bank currently
customer1 = BankAccount(name="David", curr_bal=None, mini_bal=None, account_number=None, routing_number=111111111)
customer1_checking = CheckingAccount(name="David", curr_bal=1000, mini_bal=0, account_number=222222222, routing_number=111111111)
customer1_saving = SavingsAccount(name="David", account_number=333333333, curr_bal=50, mini_bal=10, routing_number=111111111)

customer2 = BankAccount(name="Ann", curr_bal=None, mini_bal=None, account_number=None, routing_number=111111111)
customer2_checking = CheckingAccount(name="Ann", curr_bal=8000, mini_bal=500, account_number=444444444, routing_number=111111111)
customer2_saving = SavingsAccount(name="Ann", account_number=555555555, curr_bal=5000, mini_bal=300, routing_number=111111111)

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
    print("2. Access Checking Account")
    print("3. Access Savings Account")
    print("4. Exit")

    choice = input("Enter the number of your choice: ")

    if choice == "1":
        # Print account information
        customer_account.print_customer_information()

    elif choice == "2":
        # Match customer name to the correct checking account and update customer_account
        if customer_name == customer1.name:
            customer_account = customer1_checking
        elif customer_name == customer2.name:
            customer_account = customer2_checking
        else:
            print("Error: Checking account not found.")
            continue  # Go back to menu

        print("Checking Account Information:")
        customer_account.print_customer_information()

        print("Your masked Checking account number is:")
        print(customer_account.get_account_number())

        customer_account.customer_action()

    elif choice == "3":
        # Match customer name to the correct checking account and update customer_account
        if customer_name == customer1.name:
            customer_account = customer1_saving
        elif customer_name == customer2.name:
            customer_account = customer2_saving
        else:
            print("Error: Checking account not found.")
            continue  # Go back to menu

        print("Savings Account Information:")
        customer_account.print_customer_information()

        print("Your masked Saving account number is:")
        print(customer_account.get_account_number())

        customer_account.customer_action()

    elif choice == "4":
        print(f"Thank you for using {customer_account.title}. Have a great day!")
        break

    else:
        print("Invalid option. Please choose again.")