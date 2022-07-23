import os


HEROKU_APP_NAME = os.getenv("HEROKU_APP_NAME")
TOKEN = os.getenv("BOT_TOKEN")
DATABASE_URL = os.getenv("DATABASE_URL")

# webhook settings
WEBHOOK_HOST = f"https://{HEROKU_APP_NAME}.herokuapp.com"
WEBHOOK_PATH = f"/webhook/{TOKEN}"
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"


# webserver settings
WEBAPP_HOST = "0.0.0.0"
WEBAPP_PORT = os.getenv("PORT", default=8000)
