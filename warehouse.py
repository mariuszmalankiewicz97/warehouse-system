import json

from product import Product


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
        for product in self.stock:
            if name == product.name:
                return product
        print(f"\nProduct: '{name}' not found\n")
        return None

    def save_to_json(self):
        temp_stock = []
        for product in self.stock:
            temp_stock.append(product.__dict__)
        with open("products.json", "w") as f:
            json.dump(temp_stock, f, indent=4)

    def load_from_json(self):
        try:
            with open("products.json", "r") as f:
                products = json.load(f)
                for product_data in products:
                    product = Product(
                        product_data["name"],
                        product_data["price"],
                        product_data["amount"],
                    )
                    self.stock.append(product)
        except FileNotFoundError:
            self.save_to_json()
            print(f"\nFile name 'products.json' don't exist!, I create for you.\n")
