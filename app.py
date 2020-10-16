from flask import Flask, render_template, request
import telebot
from telegram_post_bot import post_bot
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('telegram/post-bot', methods=['POST'])
def respond():
    post_bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "ok", 200


if __name__ == '__main__':
    app.run(debug=False)
