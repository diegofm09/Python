class BankAccount:
    def __init__(self, name, money, pin):
        self.name = name
        self._money = money
        self.__pin = pin

    def add_money(self, moneyadd):
        self._money += moneyadd

    def get_pin(self):
        print(self.__pin)

bank = BankAccount("Diego", 1200, 1234)

bank.get_pin()
bank.add_money(230)
print(bank._money)

