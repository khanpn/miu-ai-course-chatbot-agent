import pandas as pd
from .utils.singleton import Singleton
from .models import State, FeedbackEntry


@Singleton
class KnowledgeBase:
    def __init__(self):
        self._current_state = State()
        self._feedback_data = pd.DataFrame(
            {'feedback_id': [], 'percept': [], 'action_name': [], 'value': []})

    @property
    def current_state(self):
        return self._current_state

    @current_state.setter
    def current_state(self, current_state):
        return self._current_state

    def add_feedback(self, action):
        feedback_id = len(self._feedback_data) + 1
        percept = self.current_state.percept
        self._feedback_data.loc[len(self._feedback_data.index)] = [
            feedback_id, percept, action.name, None]
        return feedback_id

    def update_feedback_value(self, feedback_id, value):
        filt = self._feedback_data['feedback_id'] == feedback_id
        self._feedback_data.loc[filt, 'value'] = value
        df = self._feedback_data.loc[filt]
        row = df.iloc[0]
        return FeedbackEntry(feedback_id=row['feedback_id'], percept=row['percept'], action_name=row['action_name'], value=row['value'])

    @property
    def feedback_data(self):
        return self._feedback_data.to_json(orient='records')
