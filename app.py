from flask import Flask, render_template, request, redirect

app = Flask(__name__)

confessions = []

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        text = request.form.get("confession")
        if text:
            confessions.append(text)
        return redirect("/")
    return render_template("home.html", confessions=confessions)

if __name__ != "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=10000)
else:
    app.run(debug=True)
