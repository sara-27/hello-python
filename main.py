from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world!'

app.debug = True

app.run(port=80)
