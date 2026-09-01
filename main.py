from product import Product
from warehouse import Warehouse

warehouse: Warehouse = Warehouse()

warehouse.load_from_json()

menu_text = """\nWerehouse Menu:
1) Add product
2) View products
3) Del product
4) Change amount product
5) Change price product
6) Increase amount product
7) Decrease amount product
8) Total value product
0) Exit
Your choose: """

while True:
    try:
        menu: str | int = input(menu_text)
        if not menu:
            raise ValueError("Menu cannot be empty")
        if menu.isspace():
            raise ValueError("Menu cannot have space")
        menu = int(menu)
        if menu < 0 or menu > 8:
            raise TypeError("\nProgram accepts only integer from 0 to 8\n")
    except ValueError:
        print("Wrong value. Please enter a number from 0 to 8.")
    except TypeError:
        print("Wrong type. Please enter a valid integer.")
    else:
        if menu == 0:
            break
        elif menu == 1:
            try:
                name: str = input("Name product: ")
                price: float = float(input("Price product: "))
                amount: int = int(input("Amount product: "))
                warehouse.add_product(name, price, amount)
            except ValueError:
                print("\nPrice and amount must be a number\n")
        elif menu == 2:
            warehouse.view_products()
        elif menu == 3:
            if warehouse.check_stock():
                name: str = input("\nName product to delete: ")
                warehouse.delete_product(name)
        elif menu == 4:
            if warehouse.check_stock():
                name: str = input("Name product: ")
                product: Product | None = warehouse.find_product(name)
                if product:
                    try:
                        new_amount: int = int(input("New amount: "))
                        warehouse.change_amount_product(product, new_amount)
                    except ValueError:
                        print("\nAmount must be intiger\n")
        elif menu == 5:
            if warehouse.check_stock():
                name: str = input("\nname product: ")
                product: Product | None = warehouse.find_product(name)
                if product:
                    try:
                        new_price: float = float(input("New price: "))
                        warehouse.change_price_product(product, new_price)
                    except ValueError:
                        print("\nPrice must be a float\n")
        elif menu == 6:
            if warehouse.check_stock():
                name: str = input("Name product: ")
                product: Product | None = warehouse.find_product(name)
                if product:
                    try:
                        amount_to_add: int = int(input("How much to add: "))
                        warehouse.increase_amount_product(product, amount_to_add)
                    except ValueError:
                        print("The value must be an integer")
        elif menu == 7:
            if warehouse.check_stock():
                name: str = input("Product name: ")
                product: Product | None = warehouse.find_product(name)
                if product:
                    try:
                        amount_to_decrease: int = int(input("How much to decrease: "))
                        warehouse.decrease_amount_product(product, amount_to_decrease)
                    except ValueError as e:
                        print(e)
        elif menu == 8:
            if warehouse.check_stock():
                name: str = input("Product name: ")
                warehouse.total_value_product(name)
