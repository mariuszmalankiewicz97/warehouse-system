import json

from product import Product
from warehouse import Warehouse

warehouse = Warehouse()


def load_from_json():
    try:
        with open("products.json", "r") as f:
            products = json.load(f)
            for product_data in products:
                product = Product(
                    product_data["name"], product_data["price"], product_data["amount"]
                )
                warehouse.stock.append(product)
    except FileNotFoundError:
        save_to_json()
        print(f"\nFile name 'products.json' don't exist!, I create for you.\n")


def save_to_json():
    temp_stock = []
    for product in warehouse.stock:
        temp_stock.append(product.__dict__)
    with open("products.json", "w") as f:
        json.dump(temp_stock, f, indent=4)


load_from_json()

while True:
    try:
        menu = int(input("""\nWerehouse Menu:
1) Add product
2) View products
3) Del product
4) Change amount product
5) Change price product
6) Increase amount product
7) Decrease amount product
8) Total value product
0) Exit
Your choose: """))
    except ValueError:
        print("\nProgram akcept only integer from 1 to 8 and 0 for exit\n")
    if menu < 0 or menu > 8:
        print("\nProgram akcept only integer from 1 to 8 and 0 for exit\n")
        continue
    if menu == 0:
        break
    if not warehouse.check_stock():
        if menu == 1:
            try:
                name = input("Name product: ")
                price = float(input("Price product: "))
                amount = int(input("Amount product: "))
                product = Product(name, price, amount)
                warehouse.add_product(product)
                save_to_json()
                print(f"\nProduct add: {product}\n")
            except ValueError:
                print("\nPrice and amount must be a number\n")
    else:
        if menu == 2:
            warehouse.view_products()
        elif menu == 3:
            name = input("\nName product to delete: ")
            warehouse.delete_product(name)
            save_to_json()
        elif menu == 4:
            try:
                name = input("Name product: ")
                product = warehouse.find_product(name)
                if product:
                    current_amount = product.amount
                    print(f"\nCurrent amount: {current_amount} \n")
                    new_amount = int(input("New amount: "))
                    product.update_amount(new_amount)
                    print(
                        f"\nProduct '{name}' amount succes update from {current_amount} on {new_amount} \n"
                    )
                    save_to_json()
            except ValueError:
                print("\nAmount must be intiger\n")

        elif menu == 5:
            name = input("\nname product: ")
            product = warehouse.find_product(name)
            if product:
                try:
                    current_price = product.price
                    print(f"\nCurrent price: {current_price} \n")
                    new_price = float(input("New price: "))
                    product.update_price(new_price)
                    save_to_json()
                    print(
                        f"\nProduct '{name}' price was update from {current_price} on {new_price}\n"
                    )
                except ValueError:
                    print("\nPrice must be a float\n")
        elif menu == 6:
            name = input("Name product: ")
            product = warehouse.find_product(name)
            if product:
                try:
                    current_amount = product.amount
                    amount_to_add = int(input("How much to add: "))
                    product.increase_amount(amount_to_add)
                    print(
                        f"\nAmount increased from {current_amount} by {amount_to_add} to {product.amount}\n"
                    )
                    save_to_json()
                except ValueError:
                    print("The value must be an integer")

        elif menu == 7:
            name = input("Product name: ")
            product = warehouse.find_product(name)
            if product:
                try:
                    found = True
                    current_amount = product.amount
                    amount_to_decrease = int(input("How much to decrease: "))
                    product.decrease_amount(amount_to_decrease)
                    print(
                        f"\nDecrease amount from {current_amount} by {amount_to_decrease} to {product.amount}\n"
                    )
                    save_to_json()
                except ValueError as e:
                    print(e)
        elif menu == 8:
            name = input("Product name: ")
            product = warehouse.find_product(name)
            if product:
                print(f"\nTotal value product '{name}': {product.total_value()}\n")
