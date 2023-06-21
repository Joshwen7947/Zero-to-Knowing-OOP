class Crypto:
    def __init__(self, name):
        self.name = name
        self.price = 0
        
    def __str__(self):
        return f"This is {self.name} a cryptocurrency"
    
    def __eq__(self, other):
        if isinstance(other, Crypto):
            return self.name == other.name
        return False
    
    def __add__(self, other):
        if isinstance(other, Crypto):
            combo = self.name + " " + other.name
            return Crypto(combo)
        else:
            raise ValueError("Can not preform addtion between them!")
        
    def set_price(self, price):
        self.price += price
        
    def get_price(self):
        if hasattr(self, "price"):
            return self.price 
        else:
            print("Price not set")
            
    def calc_value(self, quantity):
        if hasattr(self, "price"):
            return self.price * quantity
        else:
            print("Price not set!")
            
            
class Bitcoin(Crypto):
    def __init__(self):
        Crypto.__init__(self,"Bitcoin")
    
    def __str__(self):
        return f"Bitcoin is decentralized!"
    
    def mine(self):
        return f"Mining the next Block..."


class Ethereum(Crypto):
    def __init__(self):
        Crypto.__init__(self,"Ethereum")
    
    def __str__(self):
        return f"Ethereum uses smart contracts!"
    
    def mine(self):
        return f"Minting tokens..."
        
        
crypto1 = Crypto("Solana")
crypto2 = Crypto("Cardano")
crypto3 = Crypto("Bitcoin")

bitcoin = Bitcoin()
ether = Ethereum()

 

print(ether + crypto2)

ether.set_price(1750)
bitcoin.set_price(28000)
crypto1.set_price(16.50)


portfolio = [
    {"crypto":bitcoin, "quantity": 5},
    {"crypto":ether, "quantity": 32},
    {"crypto":crypto1, "quantity": 25}
]

for asset in portfolio:
    crypto = asset["crypto"]
    quantity = asset["quantity"]
    
    total = crypto.calc_value(quantity)
    print(f'The total value of {crypto.name} with your amount of {quantity} is {total}')