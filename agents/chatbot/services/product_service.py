import pandas as pd
from ..utils.singleton import Singleton
from ..models.product import Product


@Singleton
class ProductService:

    def __init__(self):
        self.products = pd.read_json('data/products.json')

    def get_product_by_name(self, product_name):
        df = self.products[self.products.name.str.lower()
                           == product_name.lower()].head(1)
        if df.empty:
            return None
        return Product.from_series(df.iloc[0])

    def find_products_by_name(self, product_name):
        result = []
        self.products[self.products.name.str.contains(product_name, case=False)].apply(
            lambda row: result.append(Product.from_series(row)), axis=1)
        return result
