class Warehouse:
    def __init__(self):
        self.stock = []

    def add_product(self, product):
        self.stock.append(product)

    def view_products(self):
        if not self.stock:
            print("\nWerehouse is empty\n")
            return
        for product in self.stock:
            print(f"Product: {product}")
