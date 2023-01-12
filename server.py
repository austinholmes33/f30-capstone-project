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

# displays the users books that are being currently read and also currently not read
@app.route("/your_books")
@login_required
def your_books():
    return render_template("your_books.html")

@app.route("/add_book", methods=["POST"])
def add_book():
    form = AddBookForm()
    title = form.title.data
    author = form.author.data
    pages = form.pages.data
    overview = form.overview.data
    cover_img = form.cover_img.data

    # def __init__(title, author, pages, overview, cover_img):
    
    try:
        new_book = Book(title, author, pages, overview, cover_img)
        db.session.add(new_book) # where the primary key gets set for the book
        new_users_book = Users_book(current_user.id, new_book.id)
        db.session.add(new_users_book)
        db.session.commit()
        flash('Book Successfully Added')
        return redirect(url_for("your_books"))
    except Exception as e: # e is a variable holding the exception info
        print(e)
        print("Something went wrong")

@app.route("/update_book/<book_id>", methods=["GET", "POST"])
@login_required
def update_book(book_id):
    form = UpdateBookForm()
    book = Users_book.query.filter_by(users_id=current_user.id, books_id=book_id).first()
    if request.method == "GET":
        form.author.data = book.book.author
        form.title.data = book.book.title
        form.pages.data = book.book.pages
        form.overview.data = book.book.overview
        form.cover_img.data = book.book.cover_img
        form.pages_read.data = book.pages_read
        form.currently_reading.data = book.currently_reading
        return render_template("update_book.html", form=form, book=book)

    if request.method == "POST" and form.validate():
        print("IF STATEMENT WORKING--------------------------------------------------")
        print(current_user.id)
        print(book_id)
        updated_book = Users_book.query.filter_by(users_id=current_user.id, books_id=book_id).first()
        updated_book.pages_read = form.pages_read.data
        updated_book.currently_reading = form.currently_reading.data
        updated_book.book.title = form.title.data
        updated_book.book.author = form.author.data
        updated_book.book.pages = form.pages.data
        updated_book.book.overview = form.overview.data
        updated_book.book.cover_img = form.cover_img.data
        db.session.commit()
        flash("Book Successfully Updated")
        return redirect(url_for('your_books'))

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