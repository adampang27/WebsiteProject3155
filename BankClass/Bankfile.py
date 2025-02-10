class maltBank:
    def __init__(self, customer_name, current_balance, minimum_balance):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance

    def deposit(self, depositNum):
        self.current_balance = self.current_balance + depositNum

    def withdraw(self, withdrawNum):
        self.current_balance = self.current_balance - withdrawNum
        if self.current_balance < self.minimum_balance:
            print("Cannot make a withdrawal, not enough money!\n")
            self.current_balance = self.current_balance + withdrawNum

    def print_customer_information(self):
        print(f"Bank Title: Malt Bank")
        print(f"Customer Name: {self.customer_name}")
        print(f"Current Balance: {self.current_balance}")
        print(f"Minimum Balance: {self.minimum_balance}\n")

jack = maltBank("Jack", 1000, 0)
Billy = maltBank("Billy", 9000, 100)
jack.print_customer_information()
Billy.print_customer_information()
jack.deposit(100)
Billy.withdraw(9000)
jack.print_customer_information()
Billy.print_customer_information()