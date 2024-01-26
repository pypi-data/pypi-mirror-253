# BotForge - Telegram Bot Library

BotForge is a lightweight Python library designed to simplify the development of Telegram bots. It provides a simple interface to interact with the Telegram Bot API and includes features for handling commands.

## Features

- Easy setup for Telegram bots
- Command handling with decorators
- Simplified interaction with the Telegram Bot API

## Installation

You can install BotForge using pip:

```bash
pip install BotForge
```

## Usage

```python
# Import BotForge and necessary modules
import time
from functools import wraps
from BotForge import BotForge, CommandContext

# Initialize BotForge with your bot token
bot = BotForge(token="YOUR_BOT_TOKEN")

# Define command handlers using decorators
@bot.command_handler("/start")
def hello(ctx):
    bot.send_message(ctx.chat_id, f"Hello, {ctx.username}")

@bot.command_handler("/help")
def help_command(ctx):
    bot.send_message(ctx.chat_id, f"Hello again! {ctx.username}")

# Start the bot
bot.start()
```

## Contributing

Contributions are welcome! If you have any ideas, bug reports, or feature requests, please open an issue on the [GitHub repository](https://github.com/KailUser/BotForge).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Replace `"YOUR_BOT_TOKEN"` with the actual token of your Telegram bot. Additionally, make sure to replace the placeholder link to the GitHub repository with the actual URL once you have it.

Feel free to add more sections to the README file as needed for your project.