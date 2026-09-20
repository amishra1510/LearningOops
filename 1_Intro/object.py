class Bags:
    name = "Amritanshu"

    def details(self):
        print("Hello this a company which creates bags!")


# any variable declared outside the class but initialised with the class is an object
# an object has all the powers of a class,  it can access the methods and attributes too 


reebok = Bags()  # Object 1
campus = Bags()  # Object 2

print(Bags.name)

print(reebok.name)

print(campus.name)

reebok.details()
campus.details()
