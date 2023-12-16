from flask import Flask, render_template, request, jsonify
from agents import ChatBotAgent
from agents.chatbot import UserMessage

import random


app = Flask(__name__)
chatbot = ChatBotAgent(name='Stupid Chatbot')


@app.route("/")
def home():
    return render_template("messenger.html")


@app.route("/greeting")
def greeting():
    features = '''<ol>
        <li>Find product</li>
        <li>Add/remove product into/from shopping cart</li>
        <li>Checkout order</li>
        <li>Q/A customer service</li>
    </ol>'''
    greating = random.choice([
        '''Hi, 
        I am {}. <br/>
        I am your assistant now. <br/>
        I can support you in following topics: <br/> {} <br/>
        Please ask me everything!'''.format(chatbot.get_name(), features),

        '''Hello, my name is {}. <br/>
        I am an intelligent bot assistant.<br/>
        You can ask me any question in following topics: <br/>
        {} <br/>
        What is your question?
        '''.format(chatbot.get_name(), features),
    ])
    return jsonify({'content': greating}), 200


@app.route("/post", methods=['POST'])
def post():
    request_data = request.get_json()
    user_message = request_data['message']
    user_id = request_data['id']
    if user_id is None:
        user_id = 1
        print(
            'User ID not found, used hardcoded user_id for demonstration = {}', user_id)

    msg = chatbot.handle(UserMessage(user_message, user_id))
    return jsonify({'content': msg}), 200


if __name__ == "__main__":
    app.run()
