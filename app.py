from flask import Flask, render_template, url_for

app = Flask(__name__)
app.secret_key = "a-long-random-string"

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/base")
def base():
    return render_template("base.html")

if __name__ == "__main__":
    app.run(debug=True)


