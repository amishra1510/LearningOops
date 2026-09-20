class Building:
    def  __init__(self, building_id, building_name, energy_consumption):
        self.building_id = building_id
        self.building_name = building_name
        self.__energy_consumption = energy_consumption

    def get_energy_consumption(self):
        return self.__energy_consumption

    def set_energy_consumption(self,value):
        self.__energy_consumption = value

    def calculate_bill(self):
        return self.__energy_consumption*5
        

class SmartBuilding(Building):
    def __init__(self, building_id, building_name, energy_consumption):
        super().__init__(building_id, building_name, energy_consumption)

    def calculate_bill(self):
        return self.get_energy_consumption()*4

class IndustrialBuilding(SmartBuilding):
    def __init__(self, building_id, building_name, energy_consumption):
        super().__init__(building_id, building_name, energy_consumption)

    def calculate_bill(self):
        return self.get_energy_consumption()*6

obj = IndustrialBuilding("B004","Adani_Plant",1250)
print(obj.get_energy_consumption())
print(obj.building_name)
print(obj.building_id)
print(obj.calculate_bill())
print(isinstance(obj,IndustrialBuilding))
print(isinstance(obj,SmartBuilding))
print(isinstance(obj,Building))
print(issubclass(IndustrialBuilding,SmartBuilding))
print(issubclass(SmartBuilding,Building))
    

    