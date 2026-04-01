# inventory.py
from product import Product

class Inventory:
    def __init__(self):
        self.products = []
        self.product_id = 1

    # CREATE
    def add_product(self):
        name = input("Name: ")
        qty = int(input("Quantity: "))
        price = float(input("Price: "))

        product = Product(self.product_id, name, qty, price)
        self.products.append(product)
        self.product_id += 1
        print("Product added")

    # READ
    def view_products(self):
        if not self.products:
            print("No products available")
            return
        for p in self.products:
            p.show()

    def view_product(self):
        pid = int(input("Enter Product ID: "))
        for p in self.products:
            if p.id == pid:
                p.show()
                return
        print("Product not found")

    def view_logs(self):
        pid = int(input("Enter Product ID: "))
        for p in self.products:
            if p.id == pid:
                p.show_logs()
                return
        print("Product not found")

    # UPDATE
    def update_product(self):
        pid = int(input("Enter Product ID: "))
        for p in self.products:
            if p.id == pid:
                name = input("Enter new name: ")
                price = float(input("Enter new price: "))
                p.update(name, price)
                print("Product updated")
                return
        print("Product not found")

    def add_stock(self):
        pid = int(input("Enter Product ID: "))
        qty = int(input("Quantity to add: "))
        for p in self.products:
            if p.id == pid:
                p.add_stock(qty)
                print("Stock added")
                return
        print("Product not found")

    def remove_stock(self):
        pid = int(input("Enter Product ID: "))
        qty = int(input("Quantity to remove: "))
        for p in self.products:
            if p.id == pid:
                p.remove_stock(qty)
                return
        print("Product not found")

    # DELETE
    def delete_product(self):
        pid = int(input("Enter Product ID: "))
        for p in self.products:
            if p.id == pid:
                self.products.remove(p)
                print("Product deleted")
                return
        print("Product not found")

    def delete_out_of_stock(self):
        self.products = [p for p in self.products if p.qty > 0]
        print("Out-of-stock products removed")