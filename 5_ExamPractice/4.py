class SecureBankAccount:

    def __init__(self,owner_name,account_type,balance,pin):
        self.owner_name = owner_name
        self._account_type = account_type
        self.__balance = balance
        self.__pin = pin

    def deposit(self,amount,code):
        if code != self.__pin:
            print("Invalid code!")
        else:
            self.__balance+=amount

    def withdraw(self,amount,code):
        if code == self.__pin:
            if amount > self.__balance:
                print("Insufficient Balance")
            else:
                self.__balance-=amount 
        else:
            print("Invalid code!")

    def change_pin(self,old_pin,new_pin):
        if old_pin == self.__pin:
            self.__pin = new_pin
        else:
            print("Invalid code!")

    def get_balance(self):
        return self.__balance

class PremiumAccount(SecureBankAccount):
    def show_account(self):
        print(self.owner_name)
        print(self._account_type)
        print(self.get_balance())

obj = PremiumAccount("Aryan","Savings",15000,9981)

obj.deposit(1000,9981)
obj.withdraw(5000,9981)
obj.withdraw(5000,9982)
obj.change_pin(9981,1234)

obj.show_account()







        