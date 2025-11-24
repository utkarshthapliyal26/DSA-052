def insert_product(inventory):
    sku = input("Enter SKU: ")
    for item in inventory:
        if item['sku'] == sku:
            print("Product with this SKU already exists!")
            return
    name = input("Enter Product Name: ")
    if name.strip() == "":
        print("Product name cannot be empty.")
        return
    try:
        quantity = int(input("Enter Quantity: "))
        if quantity <= 0:
            print("Quantity must be positive.")
            return
    except ValueError:
        print("Invalid input. Quantity must be a number.")
        return
    product = {'sku': sku, 'name': name, 'quantity': quantity}
    inventory.append(product)
    print("Product inserted successfully.")

def display_inventory(inventory):
    if not inventory:
        print("Inventory is empty.")
        return
    print("SKU      Name      Quantity")
    print("-----------------------------")
    for item in inventory:
        print(f"{item['sku']}    {item['name']}    {item['quantity']}")

# Example main loop
inventory = []
while True:
    print("\nStock Manager")
    print("1. Insert New Product")
    print("2. Display Inventory")
    print("3. Exit")
    choice = input("Enter your choice (1-3): ")
    if choice == '1':
        insert_product(inventory)
    elif choice == '2':
        display_inventory(inventory)
    elif choice == '3':
        print("Exiting Inventory Manager.")
        break
    else:
        print("Invalid choice. Please select from 1 to 3.")
