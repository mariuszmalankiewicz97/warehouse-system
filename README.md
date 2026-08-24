# Warehouse System

A Python project for managing warehouse operations.

## Technologies

- Python
- Json

## Features

- Add product
- View products
- Delete product
- Change product amount
- Save and load data to json

## How it works

The application runs in the terminal and allows the user to manage warehouse products through a simple menu.

Each product contains:
- Product name
- Price
- Amount

Example:

```json
{
    "laptop": {
        "price": 5599.99,
        "amount": 11
    }
}
```

## Setup

Clone the repository:

```bash
git clone https://github.com/mariuszmalankiewicz97/warehouse-system.git
cd warehouse-system
python main.py
```