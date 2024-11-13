class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        self.products[product.product_id] = product

    def view_products(self):
        for product_id, product in self.products.items():
            print(f"ID: {product_id}, Name: {product.name}, Stock: {product.stock_quantity}")
