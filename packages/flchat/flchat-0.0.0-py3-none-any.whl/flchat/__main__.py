import os
from flask import Flask, render_template, request

from flchat.utils import get_template_folder, get_static_folder
from flchat.config import config


app = Flask(
    __name__,
    template_folder=get_template_folder(),
    static_folder=get_static_folder(),
)

@app.route("/")
def index():
    return render_template("chat.html")


@app.route("/get", methods=["GET", "POST"])
def  chat():
    input = request.form["msg"]
    return get_chat_response(input)


def get_chat_response(text):
    for step in range(5):
        return f"Step = {step} | {text}"

def run():
    app.run(host=config.FLASK_HOST, port=config.FLASK_PORT, debug=config.FLASK_DEBUG)






if __name__ == "__main__":
    run()
