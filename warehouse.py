class Warehouse:
    def __init__(self):
        self.stock = []

    def add_product(self, product):
        self.stock.append(product)

    def view_products(self):
        for product in self.stock:
            print(f"Product: {product}")

    def delete_product(self, name):
        product = self.find_product(name)

        if product:
            self.stock.remove(product)
            print(f"\nProduct {name} was delete\n")

    def check_stock(self):
        if not self.stock:
            print("\nWarehouse is empty\n")
            return False
        return True

    def find_product(self, name):
        found = False
        for product in self.stock:
            if name == product.name:
                found = True
                return product
        if not found:
            print(f"\nProduct: '{name}' not found\n")
            return None
