item_list = []

def add_item():
    item_name = input("Enter item name: ")
    item_quantity = int(input("Enter its quantity: "))
    item_price = float(input("Enter item price: "))
    item = {
        'item_name': item_name,
        'item_quantity': item_quantity,
        'item_price': item_price
    }
    item_list.append(item)
    print(f"Item {item_name} added successfully!")
    print(item_list)

def delete_item():
    item_name = input("Enter the name of the item to delete: ")
    for item in item_list:
        if item['item_name'].lower() == item_name.lower():
            item_list.remove(item)
            print(f"Item {item_name} deleted successfully!")
            return
    print(f"Item {item_name} not found.")

def update_items():
    item_name = input("Enter the name of the item to update: ")
    for item in item_list:
        if item['item_name'].lower() == item_name.lower():
            new_quantity = int(input("Enter new quantity: "))
            new_price = float(input("Enter new price: "))
            item['item_quantity'] = new_quantity
            item['item_price'] = new_price
            print(f"Item {item_name} updated successfully!")
            return
    print(f"Item {item_name} not found.")

def track_items():
    print("Current inventory:")
    for item in item_list:
        print(f"Name: {item['item_name']}, Quantity: {item['item_quantity']}, Price: ${item['item_price']:.2f}")

while True:
    tract_input = int(input("Enter 1 to add, 2 to update, 3 to delete, 4 to track items, or 5 to exit: "))
    if tract_input == 1:
        add_item()
    elif tract_input == 2:
        update_items()
    elif tract_input == 3:
        delete_item()
    elif tract_input == 4:
        track_items()
    elif tract_input == 5:
        print("Exiting...")
        break
    else:
        print("Enter a valid option.")
