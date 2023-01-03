from flask import Flask, render_template, redirect, flash, request, session
from model import db, connect_to_db
from forms import LoginForm
import crud

app = Flask(__name__)
app.secret_key = "mysecretkey"

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("books")
def all_books():    
    return render_template("books.html")

@app.route("/books/<id>")
def show_book():
    return render_template("book_details.html")

@app.route("/create_user", methods=["POST"])
def create_user():
    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email("email")

    if user:
        flash("Sorry, an account already exists with that email")
    else:
        user = crud.create_user(email, password)
        db.session.add(user)
        db.session.commit()
        flash("Account creation successful")
    return redirect("/login")


@app.route("/login", methods=["POST"])
def login_user():

    form = LoginForm(request.form)
    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email("email")

    if not user or user.password != password:
        flash("Username or password incorrect")
    else:
        session["user_email"] = user.email
        flash("Login Successful")
    return redirect("/")

@app.route("/logout")
def logout_user():
    del session["user_email"]
    flash("Logout Successful")
    return redirect("/login")

if __name__ == "__main__":
    connect_to_db(app)
    app.run(debug=True, port=5000, host="localhost")