import random


class TokenMatching:
    def __init__(self, main, linked, weights):
        self._main = main
        self._linked = linked
        self._weights = weights

    def from_series(s):
        if type(s) is not dict:
            return None
        return TokenMatching(s['main'], s['linked'], s['weights'])

    @property
    def main(self):
        return self._main

    @property
    def linked(self):
        return self._linked

    @property
    def weights(self):
        return self._weights


class Rule:
    def __init__(self, name, description, pattern, token_matching: TokenMatching, category, command, success_reply_templates, failed_reply_templates, extracted_data=None):
        self._name = name
        self._description = description
        self._pattern = pattern
        self._token_matching = token_matching
        self._category = category
        self._command = command
        self._success_reply_templates = success_reply_templates
        self._failed_reply_templates = failed_reply_templates
        self._extracted_data = extracted_data

    def from_series(s, extracted_data=None):
        token_matching = TokenMatching.from_series(s['token_matching'])
        return Rule(name=s['name'], description=s['description'], pattern=s['pattern'], token_matching=token_matching,
                    category=s['category'], command=s['command'], success_reply_templates=s['success_reply_templates'], failed_reply_templates=s['failed_reply_templates'], extracted_data=extracted_data)

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description

    @property
    def pattern(self):
        return self._pattern

    @property
    def token_matching(self):
        return self._token_matching

    @property
    def category(self):
        return self._category

    @property
    def command(self):
        return self._command

    @property
    def extracted_data(self):
        return self._extracted_data

    @property
    def success_reply_templates(self):
        return self._success_reply_templates

    @property
    def failed_reply_templates(self):
        return self._failed_reply_templates

    @property
    def random_success_reply_template(self):
        return random.choice(self._success_reply_templates)

    @property
    def random_failed_reply_template(self):
        return random.choice(self._failed_reply_templates)
