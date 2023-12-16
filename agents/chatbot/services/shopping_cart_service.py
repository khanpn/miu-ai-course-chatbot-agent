import pandas as pd
from ..utils.singleton import Singleton


class ShoppingCart:
    def __init__(self, user_id, items):
        self.user_id = user_id
        self.items = items

    def add_item(self, product, quantity=1):
        item_added = False
        for item in self.items:
            if product.__dict__['product_id'] == item['product'].__dict__['product_id']:
                item['quantity'] += quantity
                item_added = True
        if item_added is False:
            self.items.append(
                {'product': product, 'price': product.__dict__['price'], 'quantity': quantity})
        ShoppingCartService.instance().update_cart(self)

    def remove_item(self, product, quantity=1):
        found_item = None
        success = False
        for item in self.items:
            if product.__dict__['product_id'] == item['product'].__dict__['product_id']:
                if quantity < item['quantity']:
                    item['quantity'] -= quantity
                else:
                    found_item = item
                    break
                success = True
        if found_item is not None:
            self.items.remove(found_item)
        ShoppingCartService.instance().update_cart(self)
        return success


@Singleton
class ShoppingCartService:

    def __init__(self):
        self.carts = pd.DataFrame({'user_id': [], 'items': []})

    def get_cart(self, user_id):
        if self.carts[self.carts['user_id'] == user_id].empty:
            self.carts = pd.concat([self.carts, pd.DataFrame({'user_id': [user_id],
                                                              'items': [[]]})], ignore_index=True)
        return ShoppingCart(user_id, self.carts[self.carts['user_id'] == user_id].iloc[0]['items'])

    def update_cart(self, cart: 'ShoppingCart'):
        cart_filter = self.carts['user_id'] == cart.user_id
        self.carts['items'] = self.carts.loc[cart_filter,
                                             'items'].apply(lambda items: cart.items)
