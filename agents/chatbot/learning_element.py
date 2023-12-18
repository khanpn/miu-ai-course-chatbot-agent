import pandas as pd
import hashlib
from .utils.singleton import Singleton
from .rules import RuleMatcher
from .models import Action, UserMessage, ActionReward, State
from .knowledge_base import KnowledgeBase


@Singleton
class LearningElement:
    def __init__(self):
        self._learning_data = pd.DataFrame(
            {'percept': [], 'action_rewards': []})

    def make_knowledge(self, user_message: UserMessage):
        rules = RuleMatcher.instance().match_rules(user_message)
        state: State = KnowledgeBase.instance().current_state
        percept = hashlib.sha256(user_message.message.encode()).hexdigest()
        state.percept = percept

        possible_actions = list(map(lambda rule: Action(rule=rule), rules))
        if len(possible_actions) == 0:
            possible_actions.append(Action(user_message))
        state.possible_actions = possible_actions

    def receive_feedback(self, percept, action_name, new_reward):
        filt = self._learning_data['percept'] == percept
        df = self._learning_data[filt]
        if df.empty:
            self._learning_data = pd.concat([self._learning_data, pd.DataFrame({'percept': [percept],
                                                                                'action_rewards': [[ActionReward(
                                                                                    action_name=action_name, reward=new_reward)]]})], ignore_index=True)
            return

        action_rewards: list[ActionReward] = df.iloc[0]['action_rewards']
        record_exist = False
        for ar in action_rewards:
            if ar.action_name == action_name:
                ar.reward += new_reward
                record_exist = True
                break
        if not record_exist:
            action_rewards.append(ActionReward(
                action_name=action_name, reward=new_reward))

        self._learning_data.loc[filt, 'action_rewards'] = [action_rewards]

    def action_rewards(self):
        percept = KnowledgeBase.instance().current_state.percept
        df = self._learning_data.loc[self._learning_data['percept'] == percept]
        if df.empty:
            return []
        return df.iloc[0]['action_rewards']

    @property
    def learning_data(self):
        return self._learning_data.to_json(orient='records')
