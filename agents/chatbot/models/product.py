class Product:
    def __init__(self, product_id, name, description, image, price, currency, category, brand, stock_quantity):
        self._product_id = product_id
        self._name = name
        self._description = description
        self._image = image
        self._price = price
        self._currency = currency
        self._category = category
        self._brand = brand
        self._stock_quantity = stock_quantity

    def from_series(s):
        return Product(product_id=s['product_id'], name=s['name'], description=s['description'], image=s['image'], price=s['price'], currency=s['currency'], category=s['category'], brand=s['brand'], stock_quantity=s['stock_quantity'])

    @property
    def product_id(self):
        return self._product_id

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description

    @property
    def image(self):
        return self._image

    @property
    def price(self):
        return self._price

    @property
    def currency(self):
        return self._currency

    @property
    def category(self):
        return self._category

    @property
    def brand(self):
        return self._brand

    @property
    def stock_quantity(self):
        return self._stock_quantity
