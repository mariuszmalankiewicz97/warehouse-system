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
            name = input("Name product: ")
            warehouse.change_amount_product(name)
    elif menu == 5:
        if warehouse.check_stock():
            name = input("\nname product: ")
            warehouse.change_price_product(name)
    elif menu == 6:
        if warehouse.check_stock():
            name = input("Name product: ")
            warehouse.increase_amount_product(name)
    elif menu == 7:
        if warehouse.check_stock():
            name = input("Product name: ")
            warehouse.decrease_amount_product(name)

    elif menu == 8:
        if warehouse.check_stock():
            name = input("Product name: ")
            product = warehouse.find_product(name)
            if product:
                print(f"\nTotal value product '{name}': {product.total_value()}\n")
