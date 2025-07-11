from flask import Flask, render_template, request
from house_price_prediction_linear_regression_1 import askQuest
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form["username"]  # get data from input field
        greeting = askQuest(name)
        return render_template("index.html", greeting=greeting.text)
    return render_template("index.html", greeting="")

if __name__ == "__main__":
    app.run(host='192.168.56.1', port=5000, debug=False)