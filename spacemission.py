# # SAMPLE EXECUTION
# # Create objects
# cargo_ship = CargoShip("Galactic Hauler", 200, 30)
# passenger_ship = PassengerShip("Star Voyager", 100, 80)

# # Attempt to launch both ships
# cargo_ship.launch()
# # Output: Launching Galactic Hauler with cargo!
# # Fuel after launch: 200 - (50 + 30*2) = 90

# passenger_ship.launch()
# # Output: Launching Star Voyager!
# # Fuel after launch: 100 - 50 = 50

# # Refuel both ships
# cargo_ship.refuel(50)
# # Output: Refueled Galactic Hauler with 50 units. Fuel is now 140.

# passenger_ship.refuel(30)
# # Output: Refueled Star Voyager with 30 units. Fuel is now 80.

# # Launch again after refueling
# cargo_ship.launch()
# # Output: Launching Galactic Hauler with cargo!
# # Fuel after launch: 140 - (50 + 30*2) = 30

# passenger_ship.launch()
# # Output: Launching Star Voyager!
# # Fuel after launch: 80 - 50 = 30

# # Try to refuel with invalid amount
# cargo_ship.refuel(-10)
# # Output: Cannot refuel with negative amount.

# # Test PassengerShip with too many passengers
# passenger_ship.passenger_count = 120
# passenger_ship.launch()
# # Output: Too many passengers. Cannot launch.

# # Try to launch cargo ship with low fuel
# cargo_ship.launch()
# # Output: Not enough fuel to launch.

class Ship:
    def __init__(self,name,fuel):
        self.name = name
        self.fuel = fuel
    def refuel(self,amount):
        if amount < 0:
            print("Cannot refuel with negative amount.")
        else:
            self.fuel += amount
            print(f"Refueled {self.name} with {amount} units. Fuel is now {self.fuel}.")


class CargoShip(Ship):
    def __init__(self, name, fuel, cargo_weight):
        super().__init__(name, fuel)
        self.cargo_weight = cargo_weight
    
    def launch(self):
        fuel_needed = 50 + self.cargo_weight * 2
        if self.fuel >= fuel_needed:
            self.fuel -= fuel_needed
            print(f"Launching {self.name} with cargo!")
        else:
            print("Not enough fuel to launch.")

class PassengerShip(Ship):
    def __init__(self, name, fuel, passenger_count):
        super().__init__(name, fuel)
        self.passenger_count = passenger_count
    
    def launch(self):
        if self.passenger_count > 100:
            print("Too many passengers. Cannot launch.")
        elif self.fuel >= 50:
            self.fuel -= 50
            print(f"Launching {self.name}!")
        else:
            print("Not enough fuel to launch.")
            
cargo_ship = CargoShip("Galactic Hauler", 200, 30)
passenger_ship = PassengerShip("Star Voyager", 100, 80)
