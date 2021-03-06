from collections import namedtuple

from flask import Flask, render_template, redirect, url_for, request
import os

app = Flask(__name__)

Message = namedtuple('Message', 'text tag')
messages = []


@app.route('/', methods=['GET'])
def hello_world():
    return render_template('index.html')


@app.route('/login', methods=['GET'])
def main():
    return render_template('main.html', messages=messages)


@app.route('/otzivi', methods=['GET'])
def main1():
    return render_template('main.html', messages=messages)


@app.route('/add_message', methods=['POST'])
def add_message():
    text = request.form['text']
    tag = request.form['tag']

    messages.append(Message(text, tag))

    return redirect(url_for('main'))


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)