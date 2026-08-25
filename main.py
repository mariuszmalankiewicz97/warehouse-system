import json

stock = []


def load_from_json():
    try:
        with open("products.json", "r") as f:
            products = json.load(f)
            for product in products:
                stock.append(product)
    except FileNotFoundError:
        save_to_json()
        print(f"\nFile name 'products.json' don't exist!, I create for you.\n")


def save_to_json():
    with open("products.json", "w") as f:
        json.dump(stock, f, indent=4)


def add_product():
    try:
        name = input("Name product: ")
        price = float(input("Price product: "))
        amount = int(input("Amount product: "))
        product = {}
        product[name] = {"price": price, "amount": amount}
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
            if name in product:
                found = True
                print(f"\n-----{product}----\n")
                del product[name]
                save_to_json()
                print(f"\nProduct delete success: {name}\n")
                break
        if not found:
            print(f"\nProduct: '{name}' not found\n")
    else:
        print("\nWerehouse is empty\n")


def update_product():
    if stock:
        found = False
        name = input("\nname product: ")
        for product in stock:
            if name in product:
                try:
                    current_amount = product[name]["amount"]
                    print(f"\nCurrent amount: {current_amount} \n")
                    new_amount = int(input("New amount: "))
                    found = True
                    product[name] = {
                        "price": product[name]["price"],
                        "amount": new_amount,
                    }
                    save_to_json()
                    print(f"\nProduct '{name}' succes update\n")
                    break
                except ValueError:
                    print("\nAmount must be intiger\n")
        if not found:
            print(f"\nProduct '{name}' not found\n")
    else:
        print("\nWerehouse is empty\n")


load_from_json()

while True:
    try:
        menu = int(input("""\nWerehouse Menu:
1) Add product
2) View products
3) Del product
4) Change amount product
0) Exit
Your choose: """))
        if menu == 1:
            add_product()
        elif menu == 2:
            view_products()
        elif menu == 3:
            delete_product()
        elif menu == 4:
            update_product()
        elif menu == 0:
            break
    except ValueError:
        print("\nProgram akcept only intiger from 1 to 4 and 0 for exit\n")
