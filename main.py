import json

from product import Product

stock = []


def load_from_json():
    try:
        with open("products.json", "r") as f:
            products = json.load(f)
            for product_data in products:
                product = Product(
                    product_data["name"], product_data["price"], product_data["amount"]
                )
                stock.append(product)
    except FileNotFoundError:
        save_to_json()
        print(f"\nFile name 'products.json' don't exist!, I create for you.\n")


def save_to_json():
    temp_stock = []
    for product in stock:
        temp_stock.append(product.__dict__)
    with open("products.json", "w") as f:
        json.dump(temp_stock, f, indent=4)


def add_product():
    try:
        name = input("Name product: ")
        price = float(input("Price product: "))
        amount = int(input("Amount product: "))
        product = Product(name, price, amount)
        stock.append(product)
        save_to_json()
        print(f"\nProduct add success: {product}\n")
    except ValueError:
        print("\nPrice and amount must be a number\n")


def view_products():
    for product in stock:
        print(f"Product: {product}")
    if not stock:
        print("\nWerehouse is empty\n")


def delete_product():
    if stock:
        found = False
        name = input("\nName product to delete: ")
        for product in stock:
            if name == product.name:
                found = True
                stock.remove(product)
                save_to_json()
                print(f"\nProduct delete success: {name}\n")
                break
        if not found:
            print(f"\nProduct: '{name}' not found\n")
    else:
        print("\nWerehouse is empty\n")


def change_amount_product():
    if stock:
        found = False
        name = input("\nname product: ")
        for product in stock:
            if name == product.name:
                try:
                    current_amount = product.amount
                    print(f"\nCurrent amount: {current_amount} \n")
                    new_amount = int(input("New amount: "))
                    found = True
                    product.update_amount(new_amount)
                    save_to_json()
                    print(
                        f"\nProduct '{name}' amount succes update from {current_amount} on {new_amount} \n"
                    )
                    break
                except ValueError:
                    print("\nAmount must be intiger\n")
        if not found:
            print(f"\nProduct '{name}' not found\n")
    else:
        print("\nWerehouse is empty\n")


def change_price_product():
    if stock:
        found = False
        name = input("\nname product: ")
        for product in stock:
            if name == product.name:
                try:
                    current_price = product.price
                    print(f"\nCurrent price: {current_price} \n")
                    found = True
                    new_price = float(input("New price: "))
                    product.update_price(new_price)
                    save_to_json()
                    print(
                        f"\nProduct '{name}' price succes update from {current_price} on {new_price}\n"
                    )
                    break
                except ValueError:
                    print("\nPrice must be a float\n")
        if not found:
            print(f"\nProduct '{name}' not found\n")
    else:
        print("\nWerehouse is empty\n")


def increase_amount_product():
    if stock:
        found = False
        name = input("Name product: ")
        for product in stock:
            if name == product.name:
                try:
                    found = True
                    current_amount = product.amount
                    amount_to_add = int(input("How much to add: "))
                    product.increase_amount(amount_to_add)
                    print(
                        f"\nAmount increased from {current_amount} by {amount_to_add} to {product.amount}\n"
                    )
                    save_to_json()
                    break
                except ValueError:
                    print("The value must be an integer")
        if not found:
            print(f"\nProduct name '{name}' don't exist\n")
    else:
        print(f"\nWarehouse is empty\n")


def decrease_amount_product():
    if not stock:
        print("\nWarehouse is empty\n")
        return
    name = input("Product name: ")
    found = False
    for product in stock:
        if name == product.name:
            try:
                found = True
                current_amount = product.amount
                amount_to_decrease = int(input("How much to decrease: "))
                product.decrease_amount(amount_to_decrease)
                print(
                    f"\nDecrease amount from {current_amount} by {amount_to_decrease} to {product.amount}\n"
                )
                save_to_json()
                break
            except ValueError as e:
                print(e)
    if not found:
        print(f"\nProduct '{name}' not found\n")


def total_value_product():
    if not stock:
        print("\nWarehouse is empty\n")
        return
    name = input("Product name: ")
    found = False
    for product in stock:
        if name == product.name:
            found = True
            print(f"\nTotal value product '{name}': {product.total_value()}\n")
            break
    if not found:
        print(f"\nProduct name '{name}' not found")


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
        if menu == 1:
            add_product()
        elif menu == 2:
            view_products()
        elif menu == 3:
            delete_product()
        elif menu == 4:
            change_amount_product()
        elif menu == 5:
            change_price_product()
        elif menu == 6:
            increase_amount_product()
        elif menu == 7:
            decrease_amount_product()
        elif menu == 8:
            total_value_product()
        elif menu == 0:
            break
    except ValueError:
        print("\nProgram akcept only intiger from 1 to 8 and 0 for exit\n")
