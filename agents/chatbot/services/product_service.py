import pandas as pd
from ..utils.singleton import Singleton


class Product:
    def __init__(self, product_id, name, description, image, price, currency, category, brand, stock_quantity):
        self.product_id = product_id
        self.name = name
        self.description = description
        self.image = image
        self.price = price
        self.currency = currency
        self.category = category
        self.brand = brand
        self.stock_quantity = stock_quantity

    def from_series(s):
        return Product(product_id=s['product_id'], name=s['name'], description=s['description'], image=s['image'], price=s['price'], currency=s['currency'], category=s['category'], brand=s['brand'], stock_quantity=s['stock_quantity'])


@Singleton
class ProductService:

    def __init__(self):
        self.products = pd.read_json('data/products.json')

    def get_product_by_name(self, product_name):
        df = self.products[self.products['name'].str.lower()
                           == product_name.lower()].head(1)
        if df.empty:
            return None
        return Product.from_series(df.iloc[0])

    def find_products_by_name(self, product_name):
        result = []
        self.products[self.products['name'].str.contains(product_name, case=False)].apply(
            lambda row: result.append(Product.from_series(row)), axis=1)
        return result
