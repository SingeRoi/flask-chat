from flask import Flask, redirect
app = Flask(__name__)
messages = []


def add_messages(username, message):
    """Add messages to the `messages` list"""
    messages.append("{}, {}".format(username, message))


@app.route('/')
def index():
    '''Main page instructions'''
    return "To send a message use /USERNAME/MESSAGE"


@app.route('/<username>')    
def user(username):
    '''Display chat messages'''
    return "Welcome, {0} - {1}".format(username, messages)


@app.route('/<username>/<message>')
def send_message(username, message):
    """Create a new message and redirect back to the chat page"""
    add_messages(username, message)
    return redirect("/" + username)


# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)