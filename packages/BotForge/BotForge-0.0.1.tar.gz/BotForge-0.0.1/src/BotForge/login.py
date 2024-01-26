# login.py
from functools import wraps
import time
import requests
from .command_context import CommandContext


class BotForge:
    def __init__(self, token):
        self.base_url = f"https://api.telegram.org/bot{token}/"
        self.last_update_id = None
        self.command_handlers = {}

    def command_handler(self, command):
        def decorator(func):
            @wraps(func)
            def wrapper(ctx, *args, **kwargs):
                return func(ctx, *args, **kwargs)

            self.command_handlers[command] = wrapper
            return wrapper

        return decorator

    def start(self):
        while True:
            self.check_updates()
            time.sleep(0.1)  # Add a short delay to avoid excessive API requests

    def check_updates(self):
        endpoint = "getUpdates"
        params = {}
        if self.last_update_id:
            params['offset'] = self.last_update_id + 1

        response = self._make_request(endpoint, params)

        if response and response['ok']:
            for update in response['result']:
                self.last_update_id = update['update_id']
                message = update['message']

                if 'text' in message:
                    chat_id = message['chat']['id']
                    command = message['text']

                    if command in self.command_handlers:
                        ctx = CommandContext(chat_id, command, message)
                        self.command_handlers[command](ctx)

    def send_message(self, chat_id, text):
        endpoint = "sendMessage"
        params = {
            'chat_id': chat_id,
            'text': text
        }
        self._make_request(endpoint, params)

    def _make_request(self, endpoint, params):
        url = f"{self.base_url}{endpoint}"
        response = requests.get(url, params=params).json()

        if response['ok']:
            return response
        else:
            print(f"Error: {response['description']}")
            return None
