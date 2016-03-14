from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/")
def index():
    """
    home page
    """
    return render_template("index.html")

@app.route("/data", methods=["POST"])
def post_data():
    """
    post data 
    """
    pass

if __name__ == "__main__":
    app.run()
