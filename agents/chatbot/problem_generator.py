from .utils.singleton import Singleton
from .learning_element import LearningElement
from .knowledge_base import KnowledgeBase
from .models import Action, ActionReward, State
import random
import os


@Singleton
class ProblemGenerator:

    def generate(self):
        kb = KnowledgeBase.instance()
        action_rewards = LearningElement.instance().action_rewards()
        state: State = kb.current_state
        random.shuffle(state.possible_actions)
        sorted_actions = sorted(state.possible_actions, key=lambda obj: self.__get_action_sort_value(
            obj, action_rewards), reverse=True)

        if len(sorted_actions) > 1:
            state.generate_feedback = random.randint(
                0, 100) <= int(os.environ['FEEDBACK_GENERATION_RATE'])

        return sorted_actions[0]

    def __get_action_sort_value(self, action: Action, action_rewards: list[ActionReward]):
        for ar in action_rewards:
            if ar.action_name == action.name:
                return ar.reward
        return 0
