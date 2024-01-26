# command_context.py
class CommandContext:
    def __init__(self, chat_id, command, message):
        self.chat_id = chat_id
        self.command = command
        self.message = message
        self.username = message['from']['username']
