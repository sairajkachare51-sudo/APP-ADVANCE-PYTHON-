import json

# Create product data
products = {
    "products": [
        {"name": "Laptop", "quantity": 2, "price": 50000},
        {"name": "Mouse", "quantity": 5, "price": 500},
        {"name": "Keyboard", "quantity": 3, "price": 1000}
    ]
}

# Write data into JSON file
with open("products.json", "w") as file:
    json.dump(products, file, indent=4)

# Read JSON file
with open("products.json", "r") as file:
    data = json.load(file)

# Calculate total value
total = 0

for p in data["products"]:
    value = p["quantity"] * p["price"]

    print("Product:", p["name"])
    print("Quantity:", p["quantity"])
    print("Price:", p["price"])
    print("Total:", value)

    total += value

# Display final total
print("\nTotal Value of All Products:", total)