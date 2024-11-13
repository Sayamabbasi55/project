# When adding a product:
product_id = int(input("Enter product ID: "))
name = input("Enter product name: ")
category = input("Enter product category: ")
price = float(input("Enter product price: "))
stock_quantity = input("Enter product stock quantity: ")  # Stock quantity is now a string
inventory.add_product(Product(product_id, name, category, price, stock_quantity))
