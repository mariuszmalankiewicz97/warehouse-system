class Product:
    def __init__(self, name, price, amount):
        self.name = name
        self.price = price
        self.amount = amount

    def __str__(self):
        return f"name: {self.name}, price: {self.price}, amount: {self.amount}"

    def update_amount(self, amount):
        self.amount = amount

    def update_price(self, price):

        self.price = price

    def increase_amount(self, amount):
        self.amount += amount

    def decrease_amount(self, amount):
        if self.amount - amount < 0:
            raise ValueError("Amount can't be under 0")
        self.amount -= amount
