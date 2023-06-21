class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        

class ElectricCar:
    def __init__(self, battery_capacity):
        self.battery_cap = battery_capacity
    
    def charge(self):
        return self.battery_cap
    
    def get_range(self):
        return self.battery_cap * 5
    

class GasCar:
    def __init__(self, fuel_capacity):
        self.fuel_cap = fuel_capacity
    
    def refuel(self):
        return self.fuel_cap
    
    def get_fuel_range(self):
        return self.fuel_cap * 20
    

class Hybrid(Vehicle, ElectricCar, GasCar):
    def __init__(self, make, model, year, battery_capacity, fuel_capacity):
        Vehicle.__init__(self,make, model, year)
        ElectricCar.__init__(self,battery_capacity)
        GasCar.__init__(self,fuel_capacity)
        
car = Hybrid("Toyota","Prius", 2023, 5, 40)

battery_capacity = car.charge()
fuel_cap = car.refuel()
battery_range = car.get_range()
fuel_range = car.get_fuel_range()

print(f"Battery Capacity: {battery_capacity} kWh")
print(f"Fuel Capacity: {fuel_cap} gallons")
print(f"Battery Range: {battery_range} miles")
print(f"Fuel Range: {fuel_range} miles")

