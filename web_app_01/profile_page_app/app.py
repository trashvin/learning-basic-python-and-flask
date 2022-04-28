# import libraries
from flask import Flask, render_template, url_for


app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return 'hello world!'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/modern')
def index_v2():
    return render_template("index_with_bootstrap.html")


if __name__ == '__main__':
    app.run(debug=True)
