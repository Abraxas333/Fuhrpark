from datetime import datetime
from collections import defaultdict

class MotorVehicles:
    instances = []

    def __init__(self, id, kilometers, tank_capacity, license_tag, type_of_fuel):
        self.id = id
        self.kilometers = kilometers
        self.tank_capacity = tank_capacity
        self.tank = 0
        self.license_tag = license_tag
        self.type_of_fuel = type_of_fuel
        self.last_fueled = [] 
        MotorVehicles.instances.append(self)

    @classmethod
    def add_vehicle(cls, id, kilometers, tank_capacity, license_tag, type_of_fuel):
        vehicle = cls(id, kilometers, tank_capacity, license_tag, type_of_fuel)
        return vehicle

    def remove_vehicle(self):
        MotorVehicles.instances.remove(self)

    def get_vehicle_information(self):
        last_fueled_info = (f", last fueled at {self.last_fueled[-1]['timestamp']} with {self.last_fueled[-1]['amount']} liters" 
                            if self.last_fueled else "")
        return (f"Die Fahrzeug ID lautet: {self.id}, Kilometerstand beläuft sich auf {self.kilometers} und {self.tank} "
                f"Liter befinden sich im Tank, die Nummerntafel lautet {self.license_tag}, Treibstoffart: {self.type_of_fuel}{last_fueled_info}.")

    @classmethod
    def get_all_vehicles_information(cls):
        vehicles_information = [instance.get_vehicle_information() for instance in cls.instances]
        return "\n".join(vehicles_information)

    @classmethod
    def tank_up(cls, vehicle_id, amount_to_tank, type_of_fuel):
        for instance in cls.instances:
            if instance.id == vehicle_id:
                if instance.type_of_fuel != type_of_fuel:
                    print(f"Fuel type mismatch. The vehicle requires {instance.type_of_fuel}.")
                    return
                if amount_to_tank <= 0:
                    print("Amount to tank must be positive.")
                    return
                if instance.tank + amount_to_tank > instance.tank_capacity:
                    print("Amount exceeds tank capacity.")
                    return
                instance.tank += amount_to_tank
                instance.last_fueled.append({
                    'timestamp': datetime.now(),
                    'amount': amount_to_tank
                })
                print(f"Added {amount_to_tank} liters to the tank of vehicle id {vehicle_id}. Current tank amounts to {instance.tank} liters of {instance.type_of_fuel}.")
                return
        print(f"No vehicle with ID {vehicle_id} found.")

    @classmethod 
    def get_tank_by_month(cls):
        fuel_by_month = defaultdict(lambda: {'Diesel': 0, 'Benzin': 0})
        for instance in cls.instances:
            for fueling in instance.last_fueled:
                year_month = (fueling['timestamp'].year, fueling['timestamp'].month)
                fuel_by_month[year_month][instance.type_of_fuel] += fueling['amount']
        
        for (year, month), fuels in fuel_by_month.items():
            return f"Year: {year}, Month: {month}, Diesel: {fuels['Diesel']} liters, Benzin: {fuels['Benzin']} liters"
        

class LKW(MotorVehicles):
    def __init__(self, id, kilometers, tank_capacity, license_tag, type_of_fuel):
        super().__init__(id, kilometers, tank_capacity, license_tag, type_of_fuel)

class PKW(MotorVehicles):
    def __init__(self, id, kilometers, tank_capacity, license_tag, type_of_fuel):
        super().__init__(id, kilometers, tank_capacity, license_tag, type_of_fuel)

class Motorrad(MotorVehicles):
    def __init__(self, id, kilometers, tank_capacity, license_tag, type_of_fuel):
        super().__init__(id, kilometers, tank_capacity, license_tag, type_of_fuel)


Brummi = LKW(1, 253837, 70, 'G777KE', 'Diesel')
PKW1 = PKW(2, 120000, 50, 'A123BC', 'Diesel')
Motorrad1 = Motorrad(3, 30000, 15, 'B456DE', 'Benzin')


PKW2 = PKW(5, 10000, 40, 'A473OP', 'Diesel')
MotorVehicles.tank_up(5, 15, 'Diesel')
MotorVehicles.tank_up(5, 20, 'Diesel')


print(MotorVehicles.get_all_vehicles_information())


print(PKW2.get_vehicle_information())


MotorVehicles.get_tank_by_month()
