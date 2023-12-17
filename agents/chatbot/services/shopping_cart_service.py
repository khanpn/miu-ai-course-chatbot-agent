import pandas as pd
from ..utils.singleton import Singleton
from ..models.shopping_cart import ShoppingCart


@Singleton
class ShoppingCartService:

    def __init__(self):
        self.carts = pd.DataFrame({'user_id': [], 'items': []})

    def get_cart(self, user_id):
        if self.carts[self.carts['user_id'] == user_id].empty:
            self.carts = pd.concat([self.carts, pd.DataFrame({'user_id': [user_id],
                                                              'items': [[]]})], ignore_index=True)
        items = self.carts[self.carts['user_id'] == user_id].iloc[0]['items']
        return ShoppingCart(user_id, items)

    def update_cart(self, cart: ShoppingCart):
        cart_filter = self.carts['user_id'] == cart.user_id
        self.carts['items'] = self.carts.loc[cart_filter,
                                             'items'].apply(lambda items: cart.items)
