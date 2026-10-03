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









