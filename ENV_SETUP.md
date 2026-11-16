# Environment Setup

The bot reads its credentials from a local `.env` file using `python-dotenv`. You need to create this file yourself; it is not included in the repository.

## Create the file

In the same folder as `telegram.py` and `obs_grade_upd.py`, create a file named `.env` (not `.env.txt`). Add the following variables:

```dotenv
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
TELEGRAM_CHAT_ID=your_telegram_chat_id
OBS_USERNAME=your_student_number
OBS_PASSWORD=your_portal_password
```

Replace the example values with your own credentials. Do not add quotation marks unless they are part of the value.

- `TELEGRAM_BOT_TOKEN`: the token issued by BotFather when you create a Telegram bot
- `TELEGRAM_CHAT_ID`: the chat ID authorized to communicate with your bot
- `OBS_USERNAME`: your student portal username or student number
- `OBS_PASSWORD`: your student portal password

The Python scripts load these values with `load_dotenv()` and `os.getenv()`.

## Keep it private

Never upload `.env` to GitHub or share its contents. If you use Git, add this line to your local `.gitignore` before committing files:

```gitignore
.env
```

If you run the bot on another computer, create a separate `.env` file on that computer as well.

## Troubleshooting

If the bot reports missing credentials, check that the file is named exactly `.env`, that all four variable names match the examples, and that the file is in the project directory. Start the script from that directory:

```bash
python obs_grade_upd.py
```
