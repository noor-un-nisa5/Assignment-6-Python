#4. Class Variables and Class Methods
#Assignment:
#Create a class Bank with a class variable bank_name. 
#Add a class method change_bank_name(cls, name) that allows changing the bank name. Show that it affects all instances.

class Bank:
    bank_name = "Habib Bank"

    def __init__(self, account_holder):
        self.account_holder = account_holder

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

    def details(self):
        print(f"Acount Holder: {self.account_holder}, Bank: {Bank.bank_name}")

account1 = Bank("Noor")
account2 = Bank("Murk")

account1.details()
account2.details()

Bank.change_bank_name("National Bank")

account1.details()
account2.details()