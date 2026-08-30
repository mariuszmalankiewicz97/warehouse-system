class Product:
    def __init__(self, name: str, price: float, amount: int) -> None:
        self.name: str = name
        self.price: float = price
        self.amount: int = amount

    def __str__(self) -> str:
        return f"name: {self.name}, price: {self.price}, amount: {self.amount}"

    def update_amount(self, amount: int) -> None:
        self.amount = amount

    def update_price(self, price: float) -> None:
        self.price = price

    def increase_amount(self, amount: int) -> None:
        self.amount += amount

    def decrease_amount(self, amount: int) -> None:
        if self.amount - amount < 0:
            raise ValueError("Amount can't be under 0")
        self.amount -= amount

    def total_value(self) -> float:
        return self.amount * self.price
