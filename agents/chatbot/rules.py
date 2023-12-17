import regex as re
import pandas as pd
from .models.rule import Rule
from .utils.singleton import Singleton
from .services.product_service import ProductService


@Singleton
class RuleLoader:
    def __init__(self):
        self.rules_file = 'data/rules.json'

    def load_rules(self):
        return pd.read_json(self.rules_file)


@Singleton
class RuleMatcher:
    def __init__(self):
        self.rules = RuleLoader.instance().load_rules()
        self.product_names = ProductService.instance(
        ).products['name'].to_list()

    def match_rules(self, user_message):
        matched_rules = []
        initial_rule_data = {}
        for product_name in self.product_names:
            if product_name.lower() in user_message.get_message().lower():
                initial_rule_data['product_name'] = product_name

        matched_rules.extend(self.__matches_rules__(
            user_message, self.rules, initial_rule_data))
        return matched_rules

    def __matches_rules__(self, user_message, rules, initial_rule_data=None):
        matched_rules = []
        for i in range(0, len(rules)):
            extracted_rule_data = self.__extract_data_for_rule(
                user_message, initial_rule_data)
            rule = Rule.from_series(rules.iloc[i], extracted_rule_data)
            if not pd.isna(rule.pattern):
                if self.__matches_by_pattern__(user_message.get_message(), rule):
                    matched_rules.append(rule)
            elif rule.token_matching:
                if self.__matches_by_tokens__(user_message.get_message(), rule):
                    matched_rules.append(rule)

        return matched_rules

    def __matches_by_pattern__(self, sentence, rule):
        p = re.compile(str(rule.pattern))
        m = p.match(sentence.lower())
        return m is not None

    def __matches_by_tokens__(self, message, rule):
        token_matching = rule.token_matching
        main_tokens = token_matching.main
        linked_tokens = token_matching.linked
        weights = token_matching.weights.split('-')
        main_weight = 0
        linked_weight = 0
        for i in range(0, len(main_tokens)):
            if main_tokens[i].lower() in message.lower():
                main_weight += 1
        for i in range(0, len(linked_tokens)):
            if linked_tokens[i].lower() in message.lower():
                linked_weight += 1

        if main_weight < 1 or main_weight < int(weights[0]) or linked_weight < int(weights[1]):
            return False

        return True

    def __extract_data_for_rule(self, user_message, initial_rule_data=None):
        extracted_data = {'user_id': user_message.get_user_id()}
        if initial_rule_data.get('product_name'):
            product = ProductService.instance().get_product_by_name(
                initial_rule_data['product_name'])
            extracted_data['product'] = product
            numbers = re.findall(
                r'\b(\d+).*' + initial_rule_data['product_name'].lower(), user_message.message.lower())
            if len(numbers) > 0:
                extracted_data['quantity'] = int(numbers[0])
        return extracted_data
