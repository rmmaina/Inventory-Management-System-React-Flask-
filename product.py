# product.py
from datetime import datetime

class Product:
    def __init__(self, pid, name, qty, price):
        self.id = pid
        self.name = name
        self.qty = qty
        self.price = price
        self.logs = []

    def add_stock(self, amount):
        self.qty += amount
        self.logs.append(f"Added {amount} on {datetime.now()}")

    def remove_stock(self, amount):
        if amount > self.qty:
            print("Not enough stock")
            return
        self.qty -= amount
        self.logs.append(f"Removed {amount} on {datetime.now()}")

    def update(self, name, price):
        self.name = name
        self.price = price

    def show(self):
        print(f"ID: {self.id}, Name: {self.name}, Qty: {self.qty}, Price: {self.price}")

    def show_logs(self):
        if not self.logs:
            print("No logs available")
        else:
            for log in self.logs:
                print(log)