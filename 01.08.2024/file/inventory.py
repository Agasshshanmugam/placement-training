def add_item(inventory, item, quantity):
    if item in inventory:
        inventory[item] += quantity
    else:
        inventory[item] = quantity

def view_inventory(inventory):
    for item, quantity in inventory.items():
        print(f"{item}: {quantity}")

def main():
    inventory = {}
    while True:
        print("1. Add item")
        print("2. View inventory")
        print("3. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            item = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            add_item(inventory, item, quantity)
        elif choice == '2':
            view_inventory(inventory)
        elif choice == '3':
            break

if __name__ == '__main__':
    main()
