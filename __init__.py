from flask import Flask, render_template, session, request, redirect
from utils import *
from random import randint
import os

app = Flask(__name__)
app.secret_key = 'thequickbrownfoxjumpsoverthelazydog'

@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "GET":
        return render_template("index.html", username = session.get('username'))
    elif request.method == "POST":
        session['unique'] = num_rows()
        button = request.form['button']
        if button == "Sign In":
            uname = request.form.get('in_username')
            pword = request.form.get('in_password')
            if check_user(uname,pword):
                session['username'] = uname
            return render_template("index.html", username = session.get('username'))
        if button == "Sign Up":
            uname = request.form.get('up_username')
            pword = request.form.get('up_password')
            if create_user(uname, pword):
                session['username'] = uname
            return render_template("index.html", username = session.get('username'))
        return render_template("index.html", username = session.get('username'))

@app.route("/play")
def play():
    game = get_ques(session['unique'])
    session['unique'] -= 1
    return render_template("play.html", username = session.get('username'), optA = game['optA'], optB = game['optB'], optAres = game['optAres'], optBres = game['optBres'])


@app.route("/profile")
@app.route("/profile/<uname>", methods=["GET","POST"])
def profile(uname = ""):
    if os.path.isfile('./static/img/prof_pics/' + session.get('username') + '.png'):
        pic = "../static/img/prof_pics/" + session.get('username') + '.png'
    else:
        pic = "../static/img/user.png"
    if request.method == "GET":
        return render_template("profile.html", username = session.get('username'), prof_pic = pic)
    elif request.method == "POST":
        file = request.files['file']
        if file and ".png" in file.filename:
            file.save(os.getcwd() + '/static/img/prof_pics/' + session.get('username') + '.png')
            pic = "../static/img/prof_pics/" + session.get('username') + '.png'
            return render_template("profile.html", username = session.get('username'), prof_pic = pic)
        return render_template("profile.html", username = session.get('username'), prof_pic = pic)

@app.route("/logout") ##clears session
def logout():
    session['username'] = None
    session['unique'] = None
    return redirect("/")

if __name__ == "__main__":
    app.debug = True
    app.run(host = '0.0.0.0', port = 8000)
