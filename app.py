import os
from datetime import datetime
from flask import Flask, redirect, render_template, request, session, url_for
app = Flask(__name__)
messages = []

'''creates session variable'''
app =  Flask(__name__)
app.secret_key = os.getenv("SECRET",  "randomstring123")
messages =[]


def add_message(username, message):
    """Add messages to the `messages` list with timestamp"""
    now = datetime.now ().strftime("%H:%M:%S")
    messages.append({"timestamp": now, "from": username, "message": message})


@app.route('/', methods = ["GET", "POST"])
def index():
    '''Main page with instructions'''

    if request.method == "POST":
        session["username"] = request.form["username"]

    '''for existing username redirect to username variable content'''
    if "username" in session:
        return redirect(url_for("user", username=session["username"]
        ))

    return render_template("index.html")


@app.route('/chat/<username>', methods = ["GET",  "POST"])    
def user(username):
    '''Add and display chat messages'''

    if request.method == "POST":
        username = session["username"]
        message = request.form["message"]
        add_message(username, message)
        return redirect(url_for("user", username=session["username"]))
        
    return render_template("chat.html", username = username, chat_messages = messages)


# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, debug=False)