from flask import Flask, render_template , request
from flask import jsonify

app = Flask(__name__, static_url_path = '/static')

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug = True)
       