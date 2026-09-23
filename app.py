from flask import Flask, render_template, url_for

app = Flask(__name__)
app.secret_key = "a-long-random-string"

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/base")
def base():
    return render_template("base.html")

@app.route("/event")
def event():
    next_date ="2026-10-18"
    return render_template("events.html", event_date=next_date)


if __name__ == "__main__":
    app.run(debug=True)


