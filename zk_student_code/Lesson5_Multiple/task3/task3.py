class Customer:
    def __init__(self, customer_id, name):
        self.customer_id = customer_id
        self.name = name
        

class LoyaltyPoints:
    def __init__(self):
        self.points  = 0
        
    def earn_points(self, amount):
        self.points += amount
        
    def redeem_points(self, amount):
        if self.points >= amount:
            self.points -= amount
        else:
            print("Not Enough Points!")
            
    def show_point_balance(self):
        return self.points
    
class VIPcustomer(Customer, LoyaltyPoints):
    def __init__(self, customer_id, name):
        Customer.__init__(self, customer_id, name)
        LoyaltyPoints.__init__(self)
        

class Transaction:
    def __init__(self, transaction_id, customer, amount):
        self.transaction_id = transaction_id
        self.customer = customer
        self.amount = amount
        
class TransactionHistory:
    def __init__(self):
        self.transactions = []
        
    def add_transactions(self, transaction):
        self.transactions.append(transaction)
        
    def show_transactions(self):
        for transaction in self.transactions:
            print(transaction.transaction_id, transaction.customer.name, transaction.amount)
            
        
    
vip = VIPcustomer("VIP001","Josh")
vip.earn_points(40000)
vip.redeem_points(12500)

transaction1 = Transaction("T-001",vip, "+40000")
transaction2 = Transaction("T-002",vip,"-12500")

transaction_history = TransactionHistory()
transaction_history.add_transactions(transaction1)
transaction_history.add_transactions(transaction2)

transaction_history.show_transactions()

balance = vip.show_point_balance()

print(f"Customer ID: {vip.customer_id}")
print(f'Customer Name: {vip.name}')
print(f'Loyalty Point Balance: {balance}')