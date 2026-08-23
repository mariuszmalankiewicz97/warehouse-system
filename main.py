stock = []

while True:
    menu = int(input("""Werehouse Menu:
1) Add product
9) Exit 
Your choose: """))
    if menu == 1:
        name = input("Name product: ")
        price = input("Price product: ")
        amount = input("Amount product: ")
        product = {}
        product[name] = {price, amount}
        stock.append(product)
        print(stock)
    if menu == 9:
        break
