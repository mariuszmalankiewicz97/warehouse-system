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


# def change_price_product():
#     if stock:
#         found = False
#         name = input("\nname product: ")
#         for product in stock:
#             if name == product.name:
#                 try:
#                     current_price = product.price
#                     print(f"\nCurrent price: {current_price} \n")
#                     found = True
#                     new_price = float(input("New price: "))
#                     product.update_price(new_price)
#                     save_to_json()
#                     print(
#                         f"\nProduct '{name}' price succes update from {current_price} on {new_price}\n"
#                     )
#                     break
#                 except ValueError:
#                     print("\nPrice must be a float\n")
#         if not found:
#             print(f"\nProduct '{name}' not found\n")
#     else:
#         print("\nWerehouse is empty\n")


# def increase_amount_product():
#     if stock:
#         found = False
#         name = input("Name product: ")
#         for product in stock:
#             if name == product.name:
#                 try:
#                     found = True
#                     current_amount = product.amount
#                     amount_to_add = int(input("How much to add: "))
#                     product.increase_amount(amount_to_add)
#                     print(
#                         f"\nAmount increased from {current_amount} by {amount_to_add} to {product.amount}\n"
#                     )
#                     save_to_json()
#                     break
#                 except ValueError:
#                     print("The value must be an integer")
#         if not found:
#             print(f"\nProduct name '{name}' don't exist\n")
#     else:
#         print(f"\nWarehouse is empty\n")


# def decrease_amount_product():
#     if not stock:
#         print("\nWarehouse is empty\n")
#         return
#     name = input("Product name: ")
#     found = False
#     for product in stock:
#         if name == product.name:
#             try:
#                 found = True
#                 current_amount = product.amount
#                 amount_to_decrease = int(input("How much to decrease: "))
#                 product.decrease_amount(amount_to_decrease)
#                 print(
#                     f"\nDecrease amount from {current_amount} by {amount_to_decrease} to {product.amount}\n"
#                 )
#                 save_to_json()
#                 break
#             except ValueError as e:
#                 print(e)
#     if not found:
#         print(f"\nProduct '{name}' not found\n")


# def total_value_product():
#     if not stock:
#         print("\nWarehouse is empty\n")
#         return
#     name = input("Product name: ")
#     found = False
#     for product in stock:
#         if name == product.name:
#             found = True
#             print(f"\nTotal value product '{name}': {product.total_value()}\n")
#             break
#     if not found:
#         print(f"\nProduct name '{name}' not found")


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

        # elif menu == 5:
        #     change_price_product()
        # elif menu == 6:
        #     increase_amount_product()
        # elif menu == 7:
        #     decrease_amount_product()
        # elif menu == 8:
        #     total_value_product()
