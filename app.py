from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Waleed!'

@app.route('/server')
def server():
    return render_template('index.html')