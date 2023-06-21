class App:
    def __init__(self, users, storage, username):
        self.users = users
        self.storage = storage
        self.username = username
        
    def login(self):
        if self.username == "owner" and self.users >= 1:
            print("Welcome,",self.username)
            print("Your storage is:",self.storage)
        else:
            print("You are not a user!")
            
    def increase_capacity(self, number):
        self.storage += number
        print("Updated storage:",self.storage)
        
        
    def check_upgrade(self):
        if self.users >= self.storage:
            upgrade_amt = int(input("Upgrade amount: "))
            self.storage += upgrade_amt
        else:
            print("You still have:", str(self.storage - self.users), "spaces open!")

product_one = App(35, 256, "owner")




product_one.login()
product_one.increase_capacity(44)
print()

product_two = App(12, 128, "josh")
product_two.login()
product_two.check_upgrade()
