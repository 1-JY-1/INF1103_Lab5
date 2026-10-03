import json

def load_inventory(inventory):
    try:
        with open("inventory.json", "r") as file:
            data = json.load(file)
            for product in data["products"]:
                ID = product["ID"]
                name = product["name"]
                price = product["price"]
                stock = product["stock"]
                inventory.append([ID, name, price, stock])

    except FileNotFoundError:
        # Create the inventory file
        with open("inventory.json", "w") as file:
            json.dump({"products": []}, file, indent=4)

    return inventory

def save_inventory(inventory): #, product_name, quantity

    data = {
            "products": []
        }
    
    for item in inventory:
        product = {
            "ID": item[0],
            "name": item[1],
            "price": item[2],
            "stock": item[3]
        }

        data["products"].append(product)

    with open("inventory.json", "w") as file:
        json.dump(data, file, indent=4)

    print("\nSaving inventory...")
    print("Inventory saved successfully in inventory.json.\n")

    return inventory

def add_item_to_inventory(inventory, rejectedEntries):

    try:
        add_id = int(input("Enter the product ID: "))
        for item in inventory:
            if item[0] == add_id:
                print("Product ID already exists. Please enter a unique product ID.")
                return inventory, rejectedEntries
    except ValueError:
        print("Invalid input. Please enter a valid product ID.")
        return inventory, rejectedEntries

    try:
        add_product = input("Enter the product name: ")
    except ValueError:
        print("Invalid input. Please enter a valid product Name.")
        return inventory, rejectedEntries

    try:
        add_price = float(input("Enter the product price: "))
        if add_price <= 0:
            print("Invalid input. Please enter a positive number for price.")
            return inventory, rejectedEntries
    except ValueError:
        print("Invalid input. Please enter a valid product price.")
        return inventory, rejectedEntries

    try:
        add_stock = int(input("Enter the product stock: "))
        if add_stock <= 0:
            print("Invalid input. Please enter a positive number for stock.")
            return inventory, rejectedEntries
        elif add_stock > 500:
            print("Inventory cannot exceed 500 items. Please enter a smaller amount.")
            return inventory, rejectedEntries   
    except ValueError:
        print("Invalid input. Please enter a valid product stock.")
        return inventory, rejectedEntries

    inventory.append([add_id, add_product, add_price, add_stock])
    return inventory, rejectedEntries

def update_stock(inventory, rejectedEntries):

    print(inventory)

    try:
        update_id = int(input("Enter the product ID to update: "))
        for item in inventory:
            if item[0] == update_id:
                try:
                    new_stock = int(input("Enter the new stock quantity: "))
                    if new_stock < 0:
                        print("Invalid input. Please enter a positive number for stock.")
                        return inventory, rejectedEntries
                    elif new_stock > 500:
                        print("Inventory cannot exceed 500 items. Please enter a smaller amount.")
                        return inventory, rejectedEntries
                    item[3] = new_stock
                    print("\nStock updated successfully.")
                    print(f"Stock for product ID {update_id} updated to {new_stock}.\n")
                    return inventory, rejectedEntries
                except ValueError:
                    print("Invalid input. Please enter a valid stock quantity.")
                    return inventory, rejectedEntries
        print("Product ID not found.")
        return inventory, rejectedEntries
    except ValueError:
        print("Invalid input. Please enter a valid product ID.")
        return inventory, rejectedEntries

def search_product(inventory):

    try:
        search_id = int(input("Enter the product ID to search: "))
        for item in inventory:
            if item[0] == search_id:
                print(f"Product found: ID: {item[0]} | Name: {item[1]} | Price: {item[2]} | Stock: {item[3]}")
                return
        print("Product ID not found.")
    except ValueError:
        print("Invalid input. Please enter a valid product ID.")

def get_valid_input(user_input, inventory, rejectedEntries):

    # user_choice_int = user_input.isdigit()
    try:
        user_input = int(user_input)
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 6.")
        return False, inventory, rejectedEntries

    if user_input == 1:

        print("\nCurrent Inventory")
        print("===========================================================================")

        for item in inventory:
            print(f"ID: {item[0]} | Product: {item[1]} | Price: {item[2]} | Stock: {item[3]}")

        print("===========================================================================")
        return False, inventory, rejectedEntries

    elif user_input == 2:

        print("Add a new product to the inventory")

        inventory, rejectedEntries = add_item_to_inventory(inventory, rejectedEntries)

        return False, inventory, rejectedEntries
   
    elif user_input == 3:

        print("Update the stock of the product")

        inventory, rejectedEntries = update_stock(inventory, rejectedEntries)

        return False, inventory, rejectedEntries

    elif user_input == 4:

        print("search for the product")
        search_product(inventory)

        return False, inventory, rejectedEntries

    elif user_input == 5:

        inventory = save_inventory(inventory)

        return False, inventory, rejectedEntries

    elif user_input == 6:

        print("quit the app")
        return True, inventory, rejectedEntries

    else:
        print("Invalid input. Please enter a number between 1 and 6.")
        return False, inventory, rejectedEntries









# def get_product_name():

#     bcontinue = True

#     while bcontinue == True:

#         print("Enter the your product name.\n1. Phone\n2. Laptop\n3. Tablet")
#         product_name = input("Enter the product name: ")

#         if product_name == "Phone" or product_name == "Laptop" or product_name == "Tablet":
#             return product_name #get_product_number(product_name)
#         else:
#             print("Please enter the right product name")
#             bcontinue = True
            

#     print("Get product Name")

# def get_product_quantity(inventory, rejectedEntries, product_name):

#     numAmount = False

#     while numAmount == False:

#         print("===========================================================================")
#         amount = input("Enter the number of items to add: ")
#         numAmount = amount.isdigit()

#         if numAmount == False:

#             print("===========================================================================")
#             print ("Invalid input. Please enter a valid number.")
#             rejectedEntries += 1

#         elif numAmount == True:

#             if int(amount) < 0:
#                 print("===========================================================================")
#                 print("Invalid input. Please enter a positive number.")
#                 numAmount = False
#                 rejectedEntries += 1

#             else:
#                 numAmount, inventory, rejectedEntries = process_delivery_amount(numAmount, inventory, int(amount), rejectedEntries, product_name)

#                 # print(numAmount)

#                 if numAmount == True:
#                     return False, int(amount), inventory, rejectedEntries