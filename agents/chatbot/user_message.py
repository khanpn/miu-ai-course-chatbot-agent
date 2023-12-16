class UserMessage:
    def __init__(self, message, user_id):
        self.message = message
        self.user_id = user_id

    def get_message(self):
        return self.message

    def get_user_id(self):
        return self.user_id
