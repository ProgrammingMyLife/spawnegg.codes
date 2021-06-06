from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")


@app.route("/links")
def links():
    return render_template("links.html")

@app.route("/steambot")
def steambot():
  return redirect("https://steambot-website.programmingmyli.repl.co/", code=302)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)