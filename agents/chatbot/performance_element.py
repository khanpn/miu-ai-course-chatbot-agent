from .utils.singleton import Singleton
from .learning_element import LearningElement
from .problem_generator import ProblemGenerator


@Singleton
class PerformanceElement:

    def select_action(self, user_message):
        LearningElement.instance().make_knowledge(user_message)
        action = ProblemGenerator.instance().generate()
        return action
