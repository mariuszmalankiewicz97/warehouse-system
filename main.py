stock = []


def add_product():
    name = input("Name product: ")
    price = input("Price product: ")
    amount = input("Amount product: ")
    product = {}
    product[name] = {"price": price, "amount": amount}
    stock.append(product)
    print(f"Product add success: {product}")


def view_products():
    for product in stock:
        print(f"Product: {product}")
    if len(stock) == 0:
        print("\nWerehouse is empty\n")


def delete_product():
    found = False
    name = input("Name product to delete: ")
    for product in stock:
        if name in product:
            del product[name]
            found = True
            print(f"\nProduct delete success: {name}\n")
            break
    if found == False:
        print(f"\nProduct: '{name}' not found\n")


def update_product():
    found = False
    name = input("\nname product: ")
    for product in stock:
        if name in product:
            current_amount = product[name]["amount"]
            print(f"\nCurrent amount: {current_amount} \n")
            new_amount = input("New amount: ")
            product[name] = {
                "price": product[name]["price"],
                "amount": new_amount,
            }
            found = True
            print(f"Product '{name}' succes update")
            break
    if found == False:
        print(f"\nProduct '{name}' not found\n")


while True:
    menu = int(input("""Werehouse Menu:
1) Add product
2) View products
3) Del product
4) Change amount product
9) Exit 
Your choose: """))
    if menu == 1:
        add_product()
    elif menu == 2:
        view_products()
    elif menu == 3:
        delete_product()
    elif menu == 4:
        update_product()
    elif menu == 9:
        break
    else:
        print("\nChoose from 1 to 4 or 9 to exit\n")
        continue
