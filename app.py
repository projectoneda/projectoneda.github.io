# import necessary libraries
from flask import Flask, render_template
from new_scrape import stock_dict
# create instance of Flask app
app = Flask(__name__)

# List of dictionaries
stocks = stock_dict
# print(stocks)

# create route that renders index.html template
@app.route("/")
def index():

    return render_template("flask.html", stock=stocks)


if __name__ == "__main__":
    app.run(debug=True)
