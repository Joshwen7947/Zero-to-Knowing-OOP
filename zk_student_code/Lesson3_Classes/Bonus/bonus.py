class Guest:
    def __init__(self,first, last, rank, age):
        self.last_name = last
        self.first_name = first
        self.rank = int(rank)
        self.age = int(age)
        
    def guest_info(self, all_guests):
        for guest in all_guests:
            print(guest.first_name, guest.last_name, "Age:",guest.age)
            
    def loyalty_program(self,all_guests):        
        # 1. Create a list for any guest who meets certain conditions
        # 2. For every guest in my list, add their last name to the list
        # 3. This conditon MUST be met in order to be added to the list
        gold_members = [guest.last_name for guest in all_guests if guest.rank >= 10]
        if gold_members:
            print("Gold Members:")
            for member in gold_members:
                print("\tGuest:", member)
                
    def guest_avg(self, all_guests):
        total_age = 0
        for guest in all_guests:
            total_age += guest.age
        avg_age = total_age / len(all_guests)
        print("Average customer age:",avg_age)
        
        
all_guests = list()
num_guests = int(input("Enter a number of guests:  "))
for i in range(num_guests):
    data = input("First Name/Last Name/Rank/Age: ").split("/")
    # data = ["John", "Doe", "8", "45"]
    guest = Guest(data[0], data[1], int(data[2]), int(data[3]))
    all_guests.append(guest)
    
guest = all_guests[0]
guest.loyalty_program(all_guests)
guest.guest_info(all_guests)
guest.guest_avg(all_guests)   

    
