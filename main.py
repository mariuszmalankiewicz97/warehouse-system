stock = []

while True:
    name = input("Name product: ")
    price = input("Price product: ")
    amount = input("Amount product: ")
    product = {}
    product[name] = {price, amount}
    stock.append(product)
    print(stock)
