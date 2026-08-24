stock = []

while True:
    menu = int(input("""Werehouse Menu:
1) Add product
2) View products
3) Del product
9) Exit 
Your choose: """))
    if menu == 1:
        name = input("Name product: ")
        price = input("Price product: ")
        amount = input("Amount product: ")
        product = {}
        product[name] = {price, amount}
        stock.append(product)
        print(f"Product add success: {product}")
    if menu == 2:
        for product in stock:
            print(f"Product: {product}")
    if menu == 3:
        name = input("Name product to delete: ")
        for product in stock:
            if product in stock:
                del product[name]
                print(f"\nProduct delete success: {name}\n")
    if menu == 9:
        break
