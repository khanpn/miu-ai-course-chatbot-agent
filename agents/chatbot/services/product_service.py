import pandas as pd
from ..utils.singleton import Singleton
from ..models.product import Product
import os
import inflect


@Singleton
class ProductService:

    def __init__(self):
        self._products = pd.read_json(os.environ['PRODUCT_DATA_FILE'])
        self.inflect = inflect.engine()

    def tokenized_names(self):
        product_names = self._products['name'].to_list()
        product_names.extend(
            list(map(self.inflect.plural, product_names)))
        return product_names

    def get_product_by_name(self, product_name):
        products = self.find_products_by_name(product_name)
        if len(products) == 0:
            return None
        return products[0]

    def find_products_by_name(self, product_name):
        result = []
        singular_noun = self.inflect.singular_noun(product_name.lower())
        search_key = singular_noun if type(
            singular_noun) is str else product_name
        self._products[self._products.name.str.contains(search_key, case=False)].apply(
            lambda row: result.append(Product.from_series(row)), axis=1)
        return result
