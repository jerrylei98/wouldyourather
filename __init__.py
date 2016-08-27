from flask import Flask, render_template, session, request, redirect

app = Flask(__name__)
app.secret_key = 'thequickbrownfoxjumpsoverthelazydog'

@app.route("/")
def index():
    render_template("index.html")
