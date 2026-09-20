def extragreeting(func):
    def wrapper():
        print("Hello from the team!")
        func()
        print("Thank you for your visit!")

    return wrapper


@extragreeting
def greeting():
    print("Good Morning")

greeting()

# A decorator is a function,
# that adds extra behavior to another function
# without changing the original function's code.

