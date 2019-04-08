from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello():
    name = request.args.get("name") or "World"
    # return "Hello %s!" % name
    return render_template('index.html', name=name)