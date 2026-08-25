class Product:
    def __init__(self, name, price, amount):
        self.name = name
        self.price = price
        self.amount = amount

    def __str__(self):
        return f"name: {self.name}, price: {self.price}, amount: {self.amount}"

    def update_amount(self, amount):
        self.amount = amount
