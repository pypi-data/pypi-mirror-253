# test_pygram.py
import unittest
from src.BotForge import PyGram, CommandContext

class TestPyGram(unittest.TestCase):

    def test_command_handlers(self):
        bot = PyGram(token="6818157973:AAGTVEM9jmcTomKOWootIgTxakNyjdySI7g")

        @bot.command_handler("/start")
        def hello(ctx):
            bot.send_message(ctx.chat_id, f"Hello, {ctx.username}")

        @bot.command_handler("/help")
        def help_command(ctx):
            bot.send_message(ctx.chat_id, f"Hello again! {ctx.username}")

        # Perform any necessary assertions here

        # Clean up any resources if needed
        bot.start()

if __name__ == '__main__':
    unittest.main()
