# This file is to keep the bot running in replit
from flask import Flask
from multiprocessing import Process

app = Flask("")


@app.route("/")
def home():
    return "Hello. I am alive!"


def run():
    app.run(host="0.0.0.0", port=8080)


def keep_alive():
    t = Process(target=run)
    t.start()
