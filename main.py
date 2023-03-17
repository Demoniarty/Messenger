from flask import Flask, render_template, request
import json
from datetime import datetime

# загрузить сообщения из файла
def load_message():
    with open('db.json', 'r') as json_file:
        data = json.load(json_file)
    return data['messages']

# добавление новых сообщений
def add_message(sender, text):
    new_message = {
        'text': text,
        'sender': sender,
        'time': datetime.now().strftime('%H:%M')
    }
    all_messages.append(new_message)

# сохранение сообщений в файл
def save_messages():
    data = {
        'messages': all_messages
    }
    with open('db.json', 'w') as json_file:
        json.dump(data, json_file)

all_messages = load_message()

app = Flask(__name__) # создаем новое приложение
@app.route('/index') # 127.0.0.1:80/index

@app.route('/chat')
def display_chat():
    return render_template('form.html')

@app.route('/get_messages')
def get_messages():
    return {'messages': all_messages}

@app.route('/send_message')
def send_message():
    sender = request.args['name']
    text = request.args['text']
    add_message(sender, text)
    save_messages()
    return 'OK'

@app.route('/status')
def get_status():
    users = []
    for i in all_messages:
        if i['sender'] not in users:
            users.append(i['sender'])

    return {
        'Users ': len(users),
        'Messages: ': len(all_messages)
    }

def index_page():
    return 'Hello World!'

app.run(host='0.0.0.0', port=80) # строчка запуска сервера