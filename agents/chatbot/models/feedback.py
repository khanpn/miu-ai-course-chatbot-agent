class Feedback:
    def __init__(self, feedback_id, value):
        self._feedback_id = feedback_id
        self._value = value

    @property
    def feedback_id(self):
        return self._feedback_id

    @property
    def value(self):
        return self._value
