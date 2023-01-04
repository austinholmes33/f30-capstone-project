from flask import Flask, render_template, url_for, redirect, flash, request, session
from model import db, connect_to_db, User
from forms import LoginForm, CreateUserForm
import jinja2
import crud

app = Flask(__name__)
app.config["SECRET_KEY"] = "mysecretkey"
app.jinja_env.undefined = jinja2.StrictUndefined

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/books/<id>")
def show_book():
    return render_template("book_details.html")

# @app.route("/add_book", methods=["POST"])
# def add_book():
#     current_user = session.get("user_email")

#     user = crud.get_user_by_email(current_user)
#     newbook = crud.create_book(title, author, length, overview)

@app.route("/create_user", methods=["POST"])
def create_user():

    form = CreateUserForm(request.form)

    email = form.email.get("email")
    password = form.password.get("password")

    user = crud.get_user_by_email("email")

    if User.query.filter_by(user=user).first() == None:
        flash("Sorry, an account already exists with that email")
    else:
        user = crud.create_user(email, password)
        db.session.add(user)
        db.session.commit()
        flash("Account Creation Successful")
    return redirect(url_for("login_user"))


@app.route("/login", methods=["POST"])
def login_user():

    form = LoginForm(request.form)

    email = form.email.get("email")
    password = form.password.get("password")

    user = crud.get_user_by_email(email)

    if not user or user.password != password:
        flash("Username or password incorrect")
    else:
        session["user_email"] = user.email
        flash("Login Successful")
    return render_template("home.html")

@app.route("/logout")
def logout_user():
    del session["user_email"]
    flash("Logout Successful")
    return redirect(url_for("login_user"))

if __name__ == "__main__":
    connect_to_db(app)
    app.run(debug=True, port=5000, host="localhost")