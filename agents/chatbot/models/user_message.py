class UserMessage:
    def __init__(self, message, user_id):
        self._message = message
        self._user_id = user_id

    @property
    def message(self):
        return self._message

    @property
    def user_id(self):
        return self._user_id
