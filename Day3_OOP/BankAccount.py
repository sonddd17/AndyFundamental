class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, ammount):
           self.balance += ammount
           print("Your new Balance: ", self.balance)

    def withdraw(self,ammount):
         if ammount <= self.balance:
              self.balance -= ammount
              print("Your new Balance: ", self.balance)
              
         else:
              print("insufficent amount")
    def show_balance(self):
         print("Your Balance: ", self.balance)


My_account = BankAccount("Andy", 2000)

My_account.show_balance()
My_account.withdraw(1000)
My_account.withdraw(2000)
My_account.deposit(100)