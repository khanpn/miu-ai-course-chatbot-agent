from ..commands import Commands
from .rule import Rule


class Action:
    def __init__(self, rule: Rule = None):
        self._rule = rule

    def act(self, feedback_id):
        if self._rule is not None:
            func = getattr(Commands, self._rule.command)
            response = func(self._rule)
        else:
            response = 'This request will be delegated to LLM'

        return {'message': response, 'feedback_id': feedback_id}

    @property
    def name(self):
        if self._rule:
            return self._rule.name
        return 'Q/A'
