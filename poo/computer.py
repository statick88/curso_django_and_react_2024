class Computer:
    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print(f'El precio de venta es: {self.__maxprice}')

    def set_max_price(self, price):
        self.__maxprice = price

c = Computer()
c.sell() # El precio de venta es: 900

# change the price

c.__maxprice = 1000 # El precio de venta: 900
c.sell() # El precio de venta es: 900

# using setter function
c.set_max_price(1000)
c.sell() # El precio de venta es: 1000