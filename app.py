from datetime import datetime
from flask import Flask, redirect, render_template, request, session
app = Flask(__name__)
messages = []


app =  Flask(__name__)
app.secret_key = "randomstring123"
messages =[]


def add_messages(username, message):
    """Add messages to the `messages` list with timestamp"""
    now = datetime.now ().strftime("%H:%M:%S")
    messages_dict = {"timestamp": now, "from": username, "message": message}
    messages.append(messages_dict)


@app.route('/', methods = ["GET", "POST"])
def index():
    '''Main page with instructions'''

    if request.method == "POST":
        session["username"] = request.form["username"]

    '''for existing username redirect to username variable content'''
    if "username" in session:
        return redirect(session["username"])

    return render_template("index.html")


@app.route('/<username>')    
def user(username):
    '''Display chat messages'''
    return render_template("chat.html", username = username, chat_messages = messages)


@app.route('/<username>/<message>')
def send_message(username, message):
    """Create a new message and redirect back to the chat page"""
    add_messages(username, message)
    return redirect("/" + username)


# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)