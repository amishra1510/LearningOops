class Vehicle:

    def __init__(self, vehicle_number, vehicle_type):
        self.vehicle_number = vehicle_number
        self.vehicle_type = vehicle_type

    def maintenance_cost(self):
        return 10000


class ElectricVehicle(Vehicle):

    def __init__(self, vehicle_number, vehicle_type, battery_capacity):
        super().__init__(vehicle_number, vehicle_type)
        self.battery_capacity = battery_capacity

    def maintenance_cost(self):
        return 15000


obj = ElectricVehicle("UP16CD4212", "Car", "300KWH")

print(obj.maintenance_cost())
print(isinstance(obj, ElectricVehicle))
print(isinstance(obj, Vehicle))