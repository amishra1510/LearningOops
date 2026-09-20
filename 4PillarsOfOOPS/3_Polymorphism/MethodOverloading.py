class Hello:
    def speak(self,a):
        print(f"How are you ")
    def speak(self, a,b):
        print("How are you doing ?")

obj = Hello()
obj.speak(12,13)
#No, Python does not support traditional method overloading natively.
#If you define multiple methods with the exact same name in a Python class,
#the latest definition will overwrite all previous definitions.


#However, you can easily simulate or achieve the functionality of method overloading using
# Python’s dynamic features or built-in decorators.