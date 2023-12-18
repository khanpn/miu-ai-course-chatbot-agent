from ..commands import Commands
from .rule import Rule
from ..embedded_model.qa_chain import QAChain


class Action:
    def __init__(self, user_message=None, rule: Rule = None):
        self._rule = rule
        self._user_message = user_message

    def act(self, feedback_id):
        if self._rule is not None:
            func = getattr(Commands, self._rule.command)
            response = func(self._rule)
        else:
            response = QAChain.instance().chain(self._user_message.message)

        return {'message': response, 'feedback_id': feedback_id}

    @property
    def rule(self):
        return self._rule

    @property
    def name(self):
        if self._rule:
            return self._rule.name
        return 'Q/A'
