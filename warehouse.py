import json

from product import Product


class Warehouse:
    def __init__(self):
        self.stock = []

    def add_product(self, name, price, amount):
        product = Product(name, price, amount)
        self.stock.append(product)
        self.save_to_json()
        print(f"\nProduct add: {product}\n")

    def view_products(self):
        if self.check_stock():
            for product in self.stock:
                print(f"Product: {product}")

    def delete_product(self, name):
        product = self.find_product(name)
        if product:
            self.stock.remove(product)
            self.save_to_json()
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

    def change_amount_product(self, name):
        product = self.find_product(name)
        if product:
            try:
                current_amount = product.amount
                print(f"\nCurrent amount: {current_amount} \n")
                new_amount = int(input("New amount: "))
                product.update_amount(new_amount)
                print(
                    f"\nProduct '{name}' amount succes update from {current_amount} on {new_amount} \n"
                )
                self.save_to_json()
            except ValueError:
                print("\nAmount must be intiger\n")

    def change_price_product(self, name):
        product = self.find_product(name)
        if product:
            try:
                current_price = product.price
                print(f"\nCurrent price: {current_price} \n")
                new_price = float(input("New price: "))
                product.update_price(new_price)
                self.save_to_json()
                print(
                    f"\nProduct '{name}' price was update from {current_price} on {new_price}\n"
                )
            except ValueError:
                print("\nPrice must be a float\n")

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
