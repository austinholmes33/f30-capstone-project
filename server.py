from flask import Flask, render_template, url_for, redirect, flash, request, session
from model import db, connect_to_db, User
from forms import LoginForm, CreateUserForm
from flask_login import LoginManager, login_user, login_required, logout_user
import jinja2
import crud

app = Flask(__name__)
app.config["SECRET_KEY"] = "mysecretkey"
app.jinja_env.undefined = jinja2.StrictUndefined

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@app.route("/")
@login_required
def homepage():
    return render_template("home.html")

@app.route("/book_details")
@login_required
def show_book():
    return render_template("book_details.html")

# @app.route("/add_book", methods=["POST"])
# def add_book():
#     current_user = session.get("user_email")

#     user = crud.get_user_by_email(current_user)
#     newbook = crud.create_book(title, author, length, overview)

@app.route("/create_user", methods=["GET", "POST"])
def create_user():

    form = CreateUserForm()
    if request.method == "GET":
        return render_template("create_user.html", form=form)

    email = form.email.data
    password = form.password.data
    confirm_password = form.confirm_password.data
    first_name = form.first_name.data
    last_name = form.last_name.data
    user = crud.get_user_by_email("email")

    if user:
        flash("Sorry, an account already exists with that email")
    
    if password != confirm_password:
        return "Passwords do not match"
    elif password == confirm_password:
        new_user = crud.create_user(email, password, first_name, last_name)
        db.session.add(new_user)
        db.session.commit()
        flash("Account Creation Successful")
    return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():

    form = LoginForm()
    if request.method == "GET":
        return render_template("login.html", form=form)
    else:
        email = form.email.data
        password = form.password.data

        user = crud.get_user_by_email(email)

    if:
        if user.check_password(password):
            login_user(user)
            flash("Login Successful")
            return render_template("home.html")
    elif not user or user.password != password:
        flash("Username or password incorrect")

@app.route("/logout")
def logout_user():
    logout_user()
    flash("Logout Successful")
    return redirect(url_for("login"))

if __name__ == "__main__":
    connect_to_db(app)
    app.run(debug=True)