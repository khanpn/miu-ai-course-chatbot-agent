class State:
    def __init__(self):
        self._possible_actions = []
        self._percept = None
        self._generate_feedback = False

    @property
    def possible_actions(self):
        return self._possible_actions

    @possible_actions.setter
    def possible_actions(self, possible_actions):
        self._possible_actions = possible_actions

    @property
    def percept(self):
        return self._percept

    @percept.setter
    def percept(self, percept):
        self._percept = percept

    @property
    def generate_feedback(self):
        return self._generate_feedback

    @generate_feedback.setter
    def generate_feedback(self, generate_feedback):
        self._generate_feedback = generate_feedback
