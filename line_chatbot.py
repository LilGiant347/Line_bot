from flask import Flask, request, abort
import linebot

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot import LineBotApi
from linebot.exceptions import LineBotApiError
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)
linebot.LineBotApi('oW3KKHcxFNpPlwCa7izXCaDcq08qb+s4VJvQb1k0dYTrijNgzgX3dXlEtgJx+e/bygu/tfHDS65cHpbNdhTFAg1B/rHuKCFxfyQIRG7zuq6nscy4Oqlcjk/MjKSYDMKdNv5a7Yilhs+QVefRKJLFYAdB04t89/1O/w1cDnyilFU=')
line_bot_api = LineBotApi('oW3KKHcxFNpPlwCa7izXCaDcq08qb+s4VJvQb1k0dYTrijNgzgX3dXlEtgJx+e/bygu/tfHDS65cHpbNdhTFAg1B/rHuKCFxfyQIRG7zuq6nscy4Oqlcjk/MjKSYDMKdNv5a7Yilhs+QVefRKJLFYAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('b2d907cd2dfaa81fd8d0aa045bbccc05')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()
