from flask import Flask, render_template, url_for, redirect, flash, request, session
from model import db, connect_to_db, User, Book, Users_book
from forms import LoginForm, CreateUserForm, AddBookForm, UpdateBookForm
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
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
    form = AddBookForm()
    return render_template("home.html", form=form)

@app.route("/all_books")
@login_required
def all_books():
    return render_template("all_books.html")

@app.route("/add_book", methods=["POST"])
def add_book():
    form = AddBookForm()
    title = form.title.data
    author = form.author.data
    pages = form.pages.data
    overview = form.overview.data

    new_book = Book(current_user.id, title, author, pages, overview)
    try:
        db.session.add(new_book)
        db.session.commit()
        flash('Book Successfully Added')
        return redirect(url_for("home"))
    except:
        print("Something went wrong")

@app.route("/update_book", methods=["GET", "POST"])
@login_required
def update_book():
    form = UpdateBookForm()

    if request.method == "GET":
        return render_template("update_book.html", form=form)
        
    title = form.title.data
    author = form.author.data
    pages = form.pages.data
    overview = form.overview.data
    pages_read = form.pages_read.data
    currently_reading = form.currently_reading.data

    # NEED to verify how this logic should look
    if request.method == "POST" and form.validate():
        updated_book = Users_book(current_user.id, title, author, pages, overview, pages_read, currently_reading)
        db.session.add(updated_book)
        db.session.commit()
        flash("Book Successfully Updated")
        return redirect(url_for('all_books'))

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
    user = User.query.filter_by(email=email).first()

    if user:
        flash("Sorry, an account already exists with that email")
    
    if password != confirm_password:
        return "Passwords do not match"
    elif password == confirm_password:
        new_user = User(email, password, first_name, last_name)
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

    if user:
        if user.password == password:
            login_user(user)
            flash("Login Successful")
            form=AddBookForm()
            return render_template("home.html", form=form)
    elif not user or user.password != password:
        flash("Username or password incorrect")
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    logout_user()
    flash("Logout Successful")
    return redirect(url_for('login'))

if __name__ == "__main__":
    connect_to_db(app)
    app.run(debug=True)