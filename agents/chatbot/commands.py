from jinja2 import Environment, FileSystemLoader
from .services.product_service import ProductService
from .services.shopping_cart_service import ShoppingCartService


class Commands:
    env = Environment(loader=FileSystemLoader(
        './agents/chatbot/templates'))

    def find_products_by_name(rule):
        if not rule.extracted_data.get('product', None):
            return str(rule.get_random_failed_reply_templates())

        product_service = ProductService.instance()
        products = product_service.find_products_by_name(
            rule.extracted_data['product'].__dict__['name'])
        # Assumes the template is in the current directory

        # Load the template from a file
        template = Commands.env.get_template('product_list.html')
        rendered_html = template.render({'items': products})
        return str(rule.get_random_success_reply_templates()).format(rendered_html)

    def add_item_into_shopping_cart(rule):
        if not rule.extracted_data.get('product', None):
            return str(rule.get_random_failed_reply_templates())

        cart = ShoppingCartService.instance().get_cart(
            rule.extracted_data['user_id'])
        cart.add_item(rule.extracted_data['product'],
                      rule.extracted_data.get('quantity', 1))

        rendered_html = Commands.__get_shopping_cart_html(
            cart.user_id)
        return str(rule.get_random_success_reply_templates()).format(rendered_html)

    def remove_item_from_shopping_cart(rule):
        if not rule.extracted_data.get('product', None):
            return str(rule.get_random_failed_reply_templates())

        cart = ShoppingCartService.instance().get_cart(
            rule.extracted_data['user_id'])
        success = cart.remove_item(rule.extracted_data['product'],
                                   rule.extracted_data.get('quantity', 1))
        if not success:
            return str(rule.get_random_failed_reply_templates())

        return str(rule.get_random_success_reply_templates())

    def display_shopping_cart(rule):
        cart = ShoppingCartService.instance().get_cart(
            rule.extracted_data['user_id'])
        if len(cart.items) == 0:
            return str(rule.get_random_failed_reply_templates())

        rendered_html = Commands.__get_shopping_cart_html(
            rule.extracted_data['user_id'])
        return str(rule.get_random_success_reply_templates()).format(rendered_html)

    def __get_shopping_cart_html(user_id):
        cart = ShoppingCartService.instance().get_cart(user_id)
        # Load the template from a file
        template = Commands.env.get_template('shopping_cart.html')
        total = format(sum((item['quantity'] * item['price'])
                       for item in cart.items), '.2f')
        return template.render(
            {'items': cart.items, 'total': total})
