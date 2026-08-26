class Warehouse:
    def __init__(self):
        self.stock = []

    def add_product(self, product):
        self.stock.append(product)

    def view_products(self):
        if not self.stock:
            print("\nWarehouse is empty\n")
            return
        for product in self.stock:
            print(f"Product: {product}")

    def delete_product(self, name):
        if not self.stock:
            print("\nWarehouse is empty\n")
            return
        found = False
        for product in self.stock:
            if name == product.name:
                found = True
                self.stock.remove(product)
                print(f"\nProduct delete success: {name}\n")
                break
        if not found:
            print(f"\nProduct: '{name}' not found\n")
