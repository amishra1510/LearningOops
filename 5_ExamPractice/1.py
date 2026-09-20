class BankAccount :

    def __init__(self,account_number,customer_name,balance):
        self.account_number = account_number
        self.customer_name = customer_name
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def set_balance(self,value):
        if value >= 0:
            self.__balance = value
        else:
            print("Invalid Value")

    def display_details(self):
        print("Your name is : ", self.customer_name)
        print("Your account number is : ", self.account_number)
        print("Your Balance is : ", self.get_balance())

obj = BankAccount(10222201331, "Amritanshu", 10000)
obj.display_details()
obj.set_balance(5000)

print(vars(obj))