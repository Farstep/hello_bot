import os
from linebot.models import TextSendMessage
from linebot import LineBotApi

from dotenv import load_dotenv
load_dotenv()

CHANNEL_ACCESS_TOKEN = os.getenv('CHANNEL_ACCESS_TOKEN')
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)


def main():
    USER_ID = os.getenv('USER_ID')
    messages = TextSendMessage(text="hello!")
    line_bot_api.push_message(USER_ID, messages=messages)


if __name__ == "__main__":
    main()
