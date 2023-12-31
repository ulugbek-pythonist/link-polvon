from flask import Flask, render_template,flash,redirect, url_for

from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'e2d19f02276b3accc7795b1392826b604332447b'

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html",title="Home")


@app.route("/about")
def about():
    return render_template("about.html",title="About")

@app.route("/register",methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!','success')
        return redirect(url_for("home"))
    return render_template("register.html",title="Register",form=form)

@app.route("/login",methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect(url_for("home"))
    return render_template("login.html",title="Login",form=form)