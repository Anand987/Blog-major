from flask import render_template, url_for, flash, redirect
from flaskblog import app
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post

posts = [
    {
        "author": "Anand Sharma",
        "title": "Blog post 1",
        "content": "First post content",
        "date_posted": "April 28, 2020",
    },
    {
        "author": "John Doe",
        "title": "Blog post 2",
        "content": "Second post content",
        "date_posted": "April 30, 2020",
    },
    {
        "author": "Soham Nathani",
        "title": "Blog post 3",
        "content": "Third post content",
        "date_posted": "May 1, 2020",
    },
]

# HOME ROUTE
@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)


# ABOUT ROUTE
@app.route("/about")
def about():
    return render_template("about.html", title="About")


# REGISTER ROUTE
@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", "success")
        return redirect(url_for("home"))
    return render_template("register.html", title="Register", form=form)


# LOGIN ROUTE
@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@blog.com" and form.password.data == "password":
            flash("You have been logged in!", "success")
            return redirect(url_for("home"))
        else:
            flash("Login unsuccessful. Please check email and password", "danger")
    return render_template("login.html", title="Login", form=form)
