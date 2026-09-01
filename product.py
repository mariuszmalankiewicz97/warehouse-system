class Product:
    def __init__(self, name: str, price: float, amount: int) -> None:
        self._validate_name(name)
        self._validate_price(price)
        self._validate_amount(amount)

        self.name: str = name
        self.price: float = price
        self.amount: int = amount

    def __str__(self) -> str:
        return f"name: {self.name}, price: {self.price}, amount: {self.amount}"

    def update_amount(self, amount: int) -> None:
        self._validate_amount(amount)
        if self._validate_amount_greater_than_number(amount):
            self.amount = amount

    def update_price(self, price: float) -> None:
        self._validate_price(price)
        self.price = price

    def increase_amount(self, amount: int) -> None:
        self._validate_amount(amount)
        if self._validate_amount_greater_than_number(amount):
            self.amount += amount

    def decrease_amount(self, amount: int) -> None:
        self._validate_amount(amount)
        if (
            self._validate_amount_greater_than_number(amount)
            and self.amount - amount >= 0
        ):
            self.amount -= amount
        else:
            raise ValueError("amount cannot be below zero")

    def total_value(self) -> float:
        return self.amount * self.price

    def _validate_name(self, name: str) -> None:
        if not name:
            raise ValueError("Name can't be empty")
        if not isinstance(name, str):
            raise TypeError("Name must be string")

    def _validate_price(self, price: float) -> None:
        if price < 0:
            raise ValueError("Price must be greater than or equal to zero")
        if not isinstance(price, float):
            raise TypeError("Price must be float")

    def _validate_amount(self, amount: int) -> None:
        if amount < 0:
            raise ValueError("Amount must be greater than or equal to zero")
        if not isinstance(amount, int):
            raise TypeError("Amount must be integer")

    def _validate_amount_greater_than_number(
        self, amount: int, number: int = 0
    ) -> bool:
        if amount > number:
            return True
        raise ValueError("amount cannot be less or equal zero")
