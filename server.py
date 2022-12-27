from flask import flask, render_template, redirect, url_for, flash, request, session
from model import db, connect_to_db
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

@app.route("/users", methods=["POST"])
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
    return redirect("/")


@app.route("/login", methods=["POST"])
def login_user():
    email = request.form.get("email")
    password = request.form.get("password")

    user = cred.get_user_by_email("email")

    if not user or user.password != password:
        flash("Username or password incorrect")
    else:
        session["user_email"] = user.email
        flash("Login Successful")
    return redirect("/")

if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)