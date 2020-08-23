from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    '''Main page instructions'''
    return "To send a message use /USERNAME/MESSAGE"


@app.route('/<username>')
def user(username):
    return "Hi " + username


@app.route('/<username>/<message>')
def send_message(username, message):
    return "{0}: {1}".format(username, message)


# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)