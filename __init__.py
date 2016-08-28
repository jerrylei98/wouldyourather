from flask import Flask, render_template, session, request, redirect

app = Flask(__name__)
app.secret_key = 'thequickbrownfoxjumpsoverthelazydog'

@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "GET":
        return render_template("index.html", username = session.get('user'))
    elif request.method == "POST":
        button = request.form('button')
        return render_template("index.html", username = session.get('user'))

@app.route("/logout")
def logout():
    session['username'] = None
    return redirect("/")

if __name__ == "__main__":
    app.debug = True
    app.run(host = '0.0.0.0', port = 8000)
