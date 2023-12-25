from .knowledge_base import KnowledgeBase
from .performance_element import PerformanceElement
from .critic import Critic


class ChatBotAgent:
    def __init__(self, name):
        self._name = name
        self._performance_element = PerformanceElement.instance()

    def handle_request(self, user_message):
        action = self._performance_element.select_action(user_message)
        if action is not None:
            kb = KnowledgeBase.instance()

            state = kb.current_state

            feedback_id = None

            if state.generate_feedback:
                feedback_id = KnowledgeBase.instance().add_feedback(action)
            return action.act(feedback_id)
        return 'Opps! something went wrong'

    def handle_feedback(self, feedback):
        Critic.instance().handle_feedback(feedback)

    @property
    def name(self):
        return self._name
