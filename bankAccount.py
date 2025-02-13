from savings_and_checking import SavingsAccount

class BankAccount:

    def __init__(self, name, curr_bal, mini_bal):

        self.title = "Turbo Credit Union"

        self.name = name
        self.curr_bal = curr_bal
        self.mini_bal = mini_bal

    def deposit(self, value):
        self.curr_bal += value

    def withdraw(self, value):
        if self.curr_bal - value < self.mini_bal:
            print('Unable to withdraw. Requested amount exceeds available funds.')
        else:
            self.curr_bal -= value

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
