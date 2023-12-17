class FeedbackEntry:
    def __init__(self, feedback_id, percept, action_name, value):
        self._feedback_id = feedback_id
        self._percept = percept
        self._action_name = action_name
        self._value = value

    @property
    def feedback_id(self):
        return self._feedback_id

    @property
    def percept(self):
        return self._percept

    @property
    def action_name(self):
        return self._action_name

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value
