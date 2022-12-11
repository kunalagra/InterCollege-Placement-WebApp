from flask import Flask
app = Flask(__name__)

from views import *
app.secret_key = "SessionKEy145"
app.config['SESSION_TYPE'] = 'filesystem'

if __name__ == "__main__":
    app.run(debug="true")