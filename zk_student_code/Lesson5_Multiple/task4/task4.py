class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        
class Customer(User):
    def __init__(self, username, email):
        super().__init__(username, email)
        self.cart = []
        
    def add_to_cart(self, product):
        self.cart.append(product)
        
    def remove_to_cart(self,product):
        if product in self.cart:
            self.cart.remove(product)
        else:
            print("Item not in your cart!")
            
    def view_cart(self):
        print("Items in cart:")
        for product in self.cart:
            print(product.name)
            
            
    # filename.txt
    def save_cart(self, filename):
        with open(filename, "w") as file:
            for product in self.cart:
                file.write(f'{product.name}, {product.price}\n')
        print(f'Cart saved to {filename}')
        


class Seller(User):
    def __init__(self, username, email):
        super().__init__(username, email)
        self.products = []
        
    def add_product(self,product):
        self.products.append(product)
    
    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)
        else:
            print(f'Product Not Found!')
    
    def view_products(self):
        print(f'List of Products:')
        for product in self.products:
            print(product.name)
    
    def save_products(self, filename):
        with open(filename,"w") as file:
            for product in self.products:
                file.write(f'{product.name}, {product.price}\n')
        print(f'Products saved to {filename}')
        
class Product:
    def __init__(self, name, price):
        self.name = name 
        self.price = price
        
    def basic_info(self):
        print(f'Product: {self.name}')
        print(f'Price: {self.price}')
        

customer = Customer("BillyBob123", "billy@hooloo.com")
seller = Seller("SarahJane88", "jane@yahoo.com")

product1 = Product("Shoes",65.00) 
product2 = Product("Ring",125.00)   
product3 = Product("T-Shirt", 28.00)   

customer.add_to_cart(product1)
customer.add_to_cart(product2)
customer.add_to_cart(product3)

customer.view_cart()

customer.save_cart("customer_cart.txt")

customer.remove_to_cart(product2)

customer.view_cart()



# 
seller.add_product(product1)
seller.add_product(product2)
seller.add_product(product3)

seller.view_products()

seller.save_products("seller_products.txt")

        
        
        
        
        
        