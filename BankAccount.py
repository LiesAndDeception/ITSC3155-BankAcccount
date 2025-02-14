import random

class BankAccount:


    def __init__(self, name, curr_bal, mini_bal):

        self.bank_name = "Turbo Credit Union"
        self.routing_number = 123456789
        self.name = name
        self.curr_bal = curr_bal
        self.mini_bal = mini_bal
        self.is_logged_in = False
        self.account_number = int(random.uniform(100000000, 999999999))
        print('The account number for ' + self.name + ' is ' + str(self.account_number))
        print('The routing number for ' + self.bank_name + ' is ' + str(self.routing_number))

    def login(self):
        entry = input("Enter your account number: ")
        if entry == str(self.account_number):
            print("Welcome. You are now logged in.")
            self.is_logged_in = True
        else: print("That number is incorrect.")

    def logout(self):
        if self.is_logged_in: self.is_logged_in = False
        else: print('You are not logged in.')

    def deposit(self, value):
        if self.is_logged_in:
            self.curr_bal += value
        else: print('You are not logged in.')

    def withdraw(self, value):
        if self.is_logged_in:
            if self.curr_bal - value < self.mini_bal:
                print('Unable to withdraw. Requested amount exceeds available funds.')
            else:
                self.curr_bal -= value
        else: print('You are not logged in.')

    def print_customer_information(self):
        if self.is_logged_in:
            print_str = self.bank_name + """ Account:
            --------------------------
            # Account Owner: """ + self.name + " ||| " + str(self.account_number) + """ 
            Current Balance: """ + str(self.curr_bal)

            print(print_str)

        # Turbo Credit Union Account:
        # --------------------------
        # Account Owner: name
        # Current Balance: curr_bal

        else:
            print('You are not logged in.')