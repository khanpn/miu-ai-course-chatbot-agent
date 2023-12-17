from .utils.singleton import Singleton
from .models import Feedback, FeedbackEntry
from .knowledge_base import KnowledgeBase
from .learning_element import LearningElement


@Singleton
class Critic:

    def handle_feedback(self, feedback: Feedback):
        kb = KnowledgeBase.instance()
        fb: FeedbackEntry = kb.update_feedback_value(
            feedback.feedback_id, feedback.value)
        reward = -1
        if feedback.value == 'positive':
            reward = 1

        LearningElement.instance().receive_feedback(
            fb.percept, fb.action_name, reward)
