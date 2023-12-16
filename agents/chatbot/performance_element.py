from .rules import RuleMatcher
from .action import Action


class PerformanceElement:
    def __init__(self):
        self.rule_matcher = RuleMatcher.instance()

    def update_state(self, request):
        self.state.append_request(request)

    def select_action(self, user_message):
        rules = self.rule_matcher.match_rules(user_message)
        action = Action()
        if rules:
            # TODO: selecting best action will be handled in learning feature
            action.rule = rules[0]

        return action
