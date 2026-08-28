from product import Product
from warehouse import Warehouse

warehouse = Warehouse()

warehouse.load_from_json()

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
        print("\nProgram akcepts only integer from 0 to 8\n")
        continue
    if menu < 0 or menu > 8:
        if menu < 0 or menu > 8:
            print("\nProgram accepts only integer from 0 to 8\n")
            continue
    elif menu == 0:
        break
    elif menu == 1:
        try:
            name = input("Name product: ")
            price = float(input("Price product: "))
            amount = int(input("Amount product: "))
            warehouse.add_product(name, price, amount)
        except ValueError:
            print("\nPrice and amount must be a number\n")
    elif menu == 2:
        warehouse.view_products()
    elif menu == 3:
        if warehouse.check_stock():
            name = input("\nName product to delete: ")
            warehouse.delete_product(name)
    elif menu == 4:
        if warehouse.check_stock():
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
                    warehouse.save_to_json()
            except ValueError:
                print("\nAmount must be intiger\n")
    elif menu == 5:
        if warehouse.check_stock():
            name = input("\nname product: ")
            product = warehouse.find_product(name)
            if product:
                try:
                    current_price = product.price
                    print(f"\nCurrent price: {current_price} \n")
                    new_price = float(input("New price: "))
                    product.update_price(new_price)
                    warehouse.save_to_json()
                    print(
                        f"\nProduct '{name}' price was update from {current_price} on {new_price}\n"
                    )
                except ValueError:
                    print("\nPrice must be a float\n")
    elif menu == 6:
        if warehouse.check_stock():
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
                    warehouse.save_to_json()
                except ValueError:
                    print("The value must be an integer")

    elif menu == 7:
        if warehouse.check_stock():
            name = input("Product name: ")
            product = warehouse.find_product(name)
            if product:
                try:
                    current_amount = product.amount
                    amount_to_decrease = int(input("How much to decrease: "))
                    product.decrease_amount(amount_to_decrease)
                    print(
                        f"\nDecrease amount from {current_amount} by {amount_to_decrease} to {product.amount}\n"
                    )
                    warehouse.save_to_json()
                except ValueError as e:
                    print(e)
    elif menu == 8:
        if warehouse.check_stock():
            name = input("Product name: ")
            product = warehouse.find_product(name)
            if product:
                print(f"\nTotal value product '{name}': {product.total_value()}\n")
