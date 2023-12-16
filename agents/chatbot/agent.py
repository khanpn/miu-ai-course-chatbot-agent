
from .performance_element import PerformanceElement


class ChatBotAgent:
    def __init__(self, name):
        self.name = name
        self.performance_element = PerformanceElement()

    def handle(self, user_message):
        action = self.performance_element.select_action(user_message)
        if action is not None:
            return action.act()
        return 'Opps! something went wrong'

    def get_name(self):
        return self.name
