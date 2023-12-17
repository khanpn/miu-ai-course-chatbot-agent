
class ActionReward:
    def __init__(self, action_name, reward=0):
        self._action_name = action_name
        self._reward = reward

    @property
    def action_name(self):
        return self._action_name

    @property
    def reward(self):
        return self._reward

    @reward.setter
    def reward(self, reward):
        self._reward = reward
