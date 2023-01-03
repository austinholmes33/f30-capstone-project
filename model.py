import os
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy

class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=True)

    def __repr__(self):
        return f"User id={self.id} email{self.email}"

class Book(db.Model):

    __tablename__ = "books"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.String, nullable=False)
    length = db.Column(db.Integer, nullable=False)
    overview = db.Column(db.String, nullable=True)

    def __repr__(self):
        return f"Book title {self.title}"

class Users_book(db.Model):

    __tablename__ = "users_books"

    id = db.Column(db.Integer, autoincrement=True, primaryu_key=True)
    users_id = db.Column(db.Integer, db.ForeignKey(User.id))
    books_id = db.Column(db.Integer, db.ForeignKey(Book.id))
    pages_read = db.Column(db.Integer)
    currently_reading = db.Column(db.Boolean)

    def __repr__(self):
        return f"Users_book id{self.id}"


class Thought(db.Model):

    __tablename__ = "thoughts"

    users_books_id = db.Column(db.Integer, db.ForeignKey(Users_book.id))
    thoughts = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"Thought thoughts{self.thoughts}"



def connect_to_db(flask_app, db_uri=os.environ["DATABASE_URI"], echo=False):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app = flask_app
    print("Connected to db")


if __name__ == "__main__":
    from server import app
    connect_to_db(app)