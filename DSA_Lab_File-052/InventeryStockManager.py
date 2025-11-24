def process_sale(inventory, sku, qty_sold):
    updated_inventory = []
    sku_found = False
    for item in inventory:
        curr_sku, curr_qty = item
        if curr_sku == sku:
            sku_found = True
            if curr_qty >= qty_sold:
                updated_inventory.append((curr_sku, curr_qty - qty_sold))
                print(f"Sale processed: {qty_sold} units of SKU {sku}.")
            else:
                updated_inventory.append((curr_sku, curr_qty))
                print(f"Insufficient stock for SKU {sku}. Available: {curr_qty}")
        else:
            updated_inventory.append(item)
    if not sku_found:
        print(f"SKU {sku} not found in inventory.")
    return updated_inventory

def identify_zero_stock(inventory):
    zero_stock_list = [sku for sku, qty in inventory if qty == 0]
    if zero_stock_list:
        print("Zero stock SKUs:", zero_stock_list)
    else:
        print("No zero stock items found.")
    return zero_stock_list

# Example usage
inventory = [(101, 50), (102, 20), (103, 0)]
inventory = process_sale(inventory, 101, 30)
inventory = process_sale(inventory, 102, 25)
inventory = process_sale(inventory, 104, 10)
identify_zero_stock(inventory)
