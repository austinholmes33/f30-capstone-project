import os
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class User(db.Model, UserMixin):

    __tablename__ = "users"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=True)

    def __init__(self, email, password, first_name, last_name):
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name

# get_user_books() function associated with user

    def __repr__(self):
        return f"User id={self.id} email{self.email}"

class Book(db.Model):

    __tablename__ = "books"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.String, nullable=False)
    author = db.Column(db.String, nullable=False)
    length = db.Column(db.Integer, nullable=False)
    overview = db.Column(db.String, nullable=True)
    cover_img = db.Column(db.String, nullable=False)

    def __init__(self, title, author, length, overview, cover_img):
        self.title = title
        self.author = author
        self.length = length
        self.overview = overview
        self.cover_img = cover_img

    def __repr__(self):
        return f"Book title {self.title}"

class Users_book(db.Model):

    __tablename__ = "users_books"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    users_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    books_id = db.Column(db.Integer, db.ForeignKey("books.id"))
    pages_read = db.Column(db.Integer)
    currently_reading = db.Column(db.Boolean)

    def __init__(self, users_id, books_id, pages_read, currently_reading):
        self.users_id = users_id
        self.books_id = books_id
        self.pages_read = pages_read
        self.currently_reading = currently_reading

# get_book() gets book object from linking table

    def __repr__(self):
        return f"Users_book id{self.id}"


class Thought(db.Model):

    __tablename__ = "thoughts"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    users_books_id = db.Column(db.Integer, db.ForeignKey("users_books.id"))
    thoughts = db.Column(db.String, nullable=False)

    def __init__(self, users_books_id, thoughts):
        self.users_books_id = users_books_id
        self.thoughts = thoughts


    def __repr__(self):
        return f"Thought thoughts{self.thoughts}"



def connect_to_db(flask_app, db_uri=os.environ["DATABASE_URI"], echo=False):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app) 
    print("Connected to db")


if __name__ == "__main__":
    from server import app
    connect_to_db(app)