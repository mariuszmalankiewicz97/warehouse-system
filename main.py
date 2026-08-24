stock = []

while True:
    menu = int(input("""Werehouse Menu:
1) Add product
2) View products
3) Del product
4) Change amount product
9) Exit 
Your choose: """))
    if menu == 1:
        name = input("Name product: ")
        price = input("Price product: ")
        amount = input("Amount product: ")
        product = {}
        product[name] = {"price": price, "amount": amount}
        stock.append(product)
        print(f"Product add success: {product}")
    if menu == 2:
        for product in stock:
            print(f"Product: {product}")
    if menu == 3:
        name = input("Name product to delete: ")
        if name in stock:
            for product in stock:
                del product[name]
                print(f"\nProduct delete success: {name}\n")
        print(f"\nProduct: '{name}' not found\n")
    if menu == 4:
        name = input("\nname product: ")
        if name in stock:
            for product in stock:
                current_amount = product[name]["amount"]
                print(f"\nCurrent amount: {current_amount} \n")
                new_amount = input("New amount: ")
                product[name] = {
                    "price": product[name]["price"],
                    "amount": new_amount,
                }
        print(f"\nProduct '{name}' not found\n")
    if menu == 9:
        break
