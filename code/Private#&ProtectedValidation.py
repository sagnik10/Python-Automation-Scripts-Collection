class Bank:
    def __init__(self, balance):
        self._branch = "Main"
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError
        self.__balance = value

b = Bank(1000)
print(b.balance)
b.balance = 500
print(b.balance)
print(b._branch)
try:
    print(b.__balance)
except AttributeError as e:
    print(type(e).__name__)