class Bags:
    def __init__(self,material,zips,pockets):   #constructor function
        self.material = material
        self.zips = zips
        self.pockets = pockets

reebok = Bags("Leather", 3, 2)
campus = Bags("Polyester", 2, 4)


print(reebok.material)
print(campus.material)



 