from flask import Flask, redirect, render_template, request, session
app = Flask(__name__)
messages = []


app =  Flask(__name__)
app.secret_key = "randomstring123"
messages =[]


def add_messages(username, message):
    """Add messages to the `messages` list"""
    messages.append("{}, {}".format(username, message))


def get_all_messages():
    '''Get all messages and display separated by "/br"'''
    return "<br>".join(messages)

@app.route('/')
def index():
    '''Main page instructions'''
    return "To send a message use /USERNAME/MESSAGE"


@app.route('/<username>')    
def user(username):
    '''Display chat messages'''
    return "<h1>Welcome, {0}</h1>{1}".format(username, get_all_messages())


@app.route('/<username>/<message>')
def send_message(username, message):
    """Create a new message and redirect back to the chat page"""
    add_messages(username, message)
    return redirect("/" + username)


# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)