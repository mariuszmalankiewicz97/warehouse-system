import json

from product import Product


class Warehouse:
    def __init__(self) -> None:
        self.stock: list[Product] = []

    def add_product(self, name: str, price: float, amount: int) -> None:
        product = Product(name, price, amount)
        if self._validate_duplicate_product(product):
            self.stock.append(product)
            self.save_to_json()
            print(f"\nProduct add: {product}\n")

    def view_products(self) -> None:
        if self.check_stock():
            for product in self.stock:
                print(f"Product: {product}")

    def delete_product(self, name: str) -> None:
        product = self.find_product(name)
        if product:
            self.stock.remove(product)
            self.save_to_json()
            print(f"\nProduct {name} was delete\n")

    def check_stock(self) -> bool:
        if not self.stock:
            print("\nWarehouse is empty\n")
            return False
        return True

    def find_product(self, name: str) -> Product | None:
        name = name.lower()
        for product in self.stock:
            if name == product.name:
                return product
        print(f"\nProduct: '{name}' not found\n")
        return None

    def change_amount_product(self, product: Product, new_amount: int) -> None:
        current_amount = product.amount
        print(f"\nCurrent amount: {current_amount} \n")
        product.update_amount(new_amount)
        print(
            f"\nProduct '{product.name}' amount succes update from {current_amount} on {new_amount} \n"
        )
        self.save_to_json()

    def change_price_product(self, product: Product, new_price: float) -> None:
        current_price = product.price
        print(f"\nCurrent price: {current_price} \n")
        product.update_price(new_price)
        self.save_to_json()
        print(
            f"\nProduct '{product.name}' price was update from {current_price} on {new_price}\n"
        )

    def increase_amount_product(self, product: Product, amount_to_add: int) -> None:
        current_amount = product.amount
        product.increase_amount(amount_to_add)
        print(
            f"\nAmount increased from {current_amount} by {amount_to_add} to {product.amount}\n"
        )
        self.save_to_json()

    def decrease_amount_product(
        self, product: Product, amount_to_decrease: int
    ) -> None:
        current_amount = product.amount
        product.decrease_amount(amount_to_decrease)
        print(
            f"\nDecrease amount from {current_amount} by {amount_to_decrease} to {product.amount}\n"
        )
        self.save_to_json()

    def total_value_product(self, name: str) -> None:
        product = self.find_product(name)
        if product:
            print(f"\nTotal value product '{name}': {product.total_value()}\n")

    def save_to_json(self) -> None:
        temp_stock: list[dict] = []
        for product in self.stock:
            temp_stock.append(product.__dict__)
        with open("products.json", "w") as f:
            json.dump(temp_stock, f, indent=4)

    def load_from_json(self) -> None:
        self.stock: list[Product] = []
        try:
            with open("products.json", "r") as f:
                products: list[dict] = json.load(f)
                for product_data in products:
                    product: Product = Product(
                        product_data["name"],
                        product_data["price"],
                        product_data["amount"],
                    )
                    self.stock.append(product)
        except FileNotFoundError:
            self.save_to_json()
            print(f"\nFile name 'products.json' don't exist!, I create for you.\n")

    def _validate_duplicate_product(self, product: Product) -> bool | None:
        found = False
        for product_in_stock in self.stock:
            print(product_in_stock.name)
            print(product.name)

            if product.name == product_in_stock.name:
                found = True
                raise ValueError("Product exist in stock")
        if not found:
            return True
