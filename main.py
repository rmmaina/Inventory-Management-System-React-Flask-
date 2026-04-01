# main.py
from inventory import Inventory

def main():
    inv = Inventory()

    while True:
        print("\n--- INVENTORY MENU ---")
        print("1 Add Product")
        print("2 View All Products")
        print("3 View Product by ID")
        print("4 Update Product")
        print("5 Add Stock")
        print("6 Remove Stock")
        print("7 Delete Product")
        print("8 Delete Out-of-Stock Products")
        print("9 View Logs")
        print("0 Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            inv.add_product()
        elif choice == "2":
            inv.view_products()
        elif choice == "3":
            inv.view_product()
        elif choice == "4":
            inv.update_product()
        elif choice == "5":
            inv.add_stock()
        elif choice == "6":
            inv.remove_stock()
        elif choice == "7":
            inv.delete_product()
        elif choice == "8":
            inv.delete_out_of_stock()
        elif choice == "9":
            inv.view_logs()
        elif choice == "0":
            print("Exiting program...")
            break
        else:
            print("Invalid choice, try again")

if __name__ == "__main__":
    main()