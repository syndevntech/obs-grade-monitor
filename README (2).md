# OBS Grade Monitor

A small Python bot that checks exam results on the Eskişehir Osmangazi University student portal and sends a screenshot through Telegram.

The bot waits for a `NOT` message, opens the portal with Playwright, and asks for the verification code through Telegram. Once the code is entered, it navigates to the exam results page and sends back a screenshot. The browser closes after each request, while the bot keeps listening for new messages.

## Requirements

- Python 3.10 or newer
- Chromium (installed through Playwright)
- A Telegram bot and its chat ID
- Access to the university student portal

## Setup

Clone the repository and install the dependencies:

```bash
git clone https://github.com/YOUR_USERNAME/obs-grade-monitor.git
cd obs-grade-monitor
python -m pip install playwright requests python-dotenv
python -m playwright install chromium
```

Create a `.env` file in the project directory before starting the bot. The required variables and an example are documented in [ENV_SETUP.md](ENV_SETUP.md).

Run the bot with:

```bash
python obs_grade_upd.py
```

## Usage

1. Send `NOT` to your Telegram bot.
2. Wait for the verification image and send the code shown in it.
3. The bot logs in and sends a screenshot of the exam results page.
4. Send `NOT` again whenever you want to check your results.

The browser runs in headless mode, so it does not open a visible window. The script can also run on a Linux machine without an active desktop session.

## Files

- `obs_grade_upd.py` — browser automation and grade-check workflow
- `telegram.py` — Telegram API requests and message polling
- `ENV_SETUP.md` — local environment variable setup

## Notes

This project is intended for personal use with an account you own. It relies on the current layout of the student portal, so changes to the site may require updating the Playwright selectors.

Do not commit your `.env` file or screenshots containing personal information.
