from .product import Product


class ShoppingCartItem:
    def __init__(self, product, price, quantity):
        self._product = product
        self._price = price
        self._quantity = quantity

    def from_series(s):
        return ShoppingCartItem(s['product'], s['price'], s['quantity'])

    @property
    def product(self):
        return self._product

    @property
    def price(self):
        return self._price

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        self._quantity = quantity


class ShoppingCart:
    def __init__(self, user_id: str, items: list[ShoppingCartItem]):
        self.user_id = user_id
        self.items = items

    def add_item(self, product: Product, quantity: int = 1):
        item_added = False
        for item in self.items:
            if product.product_id == item.product.product_id:
                item.quantity += quantity
                item_added = True
        if item_added is False:
            self.items.append(
                ShoppingCartItem(product, product.price, quantity))

    def remove_item(self, product, quantity=1):
        found_item = None
        success = False
        for item in self.items:
            if product.product_id == item.product.product_id:
                success = True
                if quantity < item.quantity:
                    item.quantity -= quantity
                else:
                    found_item = item
                    break
        if found_item is not None:
            self.items.remove(found_item)
        return success
