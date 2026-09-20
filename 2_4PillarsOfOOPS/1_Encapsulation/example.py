class Hello:
    __a = 12

    @classmethod
    def info(cls):
        print(cls.__a)

obj = Hello()

obj.info()