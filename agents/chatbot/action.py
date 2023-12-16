from .commands import Commands


class Action:
    def __init__(self, args=None, rule=None):
        self.args = args
        self.rule = rule

    def act(self):
        if self.rule is not None:
            func = getattr(Commands, self.rule.command)
            return func(self.rule)
        else:
            return 'This request will be delegated to LLM'
