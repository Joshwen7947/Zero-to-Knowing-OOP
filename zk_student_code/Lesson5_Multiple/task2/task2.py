class Account: 
    def __init__(self, act_num, balance):
        self.account = act_num
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        
    def withdrawl(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Not Enough funds!")
    
    def get_balance(self):
        return self.balance
    
class InterestAccount(Account):
    def __init__(self, act_num, balance, interest_rate):
        Account.__init__(self, act_num, balance)
        self.interest_rate = interest_rate
        
    def calc_interest(self):
        return self.balance * self.interest_rate
    

class Transactions:
    def __init__(self):
        self.transactions = []
    
    def add_transaction(self, transaction):
        self.transactions.append(transaction)
        
    def history(self):
        for transaction in self.transactions:
            print(transaction)
            
            
class SavingsAccount(InterestAccount, Transactions):
    def __init__(self, account_number, balance, interest_rate):
        InterestAccount.__init__(self,account_number, balance, interest_rate)
        Transactions.__init__(self)
        
        
        
        
savings = SavingsAccount("SA001",5000,0.08)
savings.deposit(2500)
# 7500
savings.withdrawl(650)

interest = savings.calc_interest()
balance = savings.get_balance()

savings.add_transaction("Deposit: 2500")
savings.add_transaction("Withdrawl: 650")

savings.history()

print("Balance:",balance)
print("Interest:",interest)