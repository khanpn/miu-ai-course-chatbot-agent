from jinja2 import Environment, FileSystemLoader
from .services.product_service import ProductService
from .services.shopping_cart_service import ShoppingCartService
from .models.rule import Rule


class Commands:
    env = Environment(loader=FileSystemLoader(
        './agents/chatbot/templates'))

    def find_product_by_name(rule: Rule):
        if not rule.extracted_data.get('product', None):
            return str(rule.random_failed_reply_template)

        product_service = ProductService.instance()
        products = product_service.find_products_by_name(
            rule.extracted_data['product'].name)
        # Assumes the template is in the current directory

        # Load the template from a file
        template = Commands.env.get_template('product_list.html')
        rendered_html = template.render({'items': products})
        return str(rule.random_success_reply_template).format(rendered_html)

    def add_item_into_shopping_cart(rule: Rule):
        if not rule.extracted_data.get('product', None):
            return str(rule.random_failed_reply_template)

        cart = ShoppingCartService.instance().get_cart(
            rule.extracted_data['user_id'])
        cart.add_item(rule.extracted_data['product'],
                      rule.extracted_data.get('quantity', 1))

        ShoppingCartService.instance().update_cart(cart)
        rendered_html = Commands.__get_shopping_cart_html(
            cart.user_id)
        return str(rule.random_success_reply_template).format(rendered_html)

    def remove_item_from_shopping_cart(rule: Rule):
        if not rule.extracted_data.get('product', None):
            return str(rule.random_failed_reply_template)

        cart = ShoppingCartService.instance().get_cart(
            rule.extracted_data['user_id'])
        success = cart.remove_item(rule.extracted_data['product'],
                                   rule.extracted_data.get('quantity', 1))
        if not success:
            return str(rule.random_failed_reply_template)

        ShoppingCartService.instance().update_cart(cart)
        return str(rule.random_success_reply_template)

    def display_shopping_cart(rule: Rule):
        cart = ShoppingCartService.instance().get_cart(
            rule.extracted_data['user_id'])
        if len(cart.items) == 0:
            return str(rule.random_failed_reply_template)

        rendered_html = Commands.__get_shopping_cart_html(
            rule.extracted_data['user_id'])
        return str(rule.random_success_reply_template).format(rendered_html)

    def __get_shopping_cart_html(user_id):
        cart = ShoppingCartService.instance().get_cart(user_id)
        # Load the template from a file
        template = Commands.env.get_template('shopping_cart.html')
        total = format(sum((item.quantity * item.price)
                           for item in cart.items), '.2f')
        return template.render(
            {'items': cart.items, 'total': total})
