from model import db, connect_to_db, User, Book, Users_book, Thought

def create_user(email, password):
    user = User(
        email=email,
        password=password
    )

    return user

def get_user_by_id(user_id):
    return User.query.get(user_id)

def get_user_by_email(email):
    return User.query.filter_by(email=email).first()

def create_book(title, author, length, overview):
    book = Book(
        title=title,
        author=author,
        length=length,
        overview=overview
    )

    return book

def get_all_books():
    return Book.query.all()

if __name__ == "__main__":
    from server import app
    connect_to_db(app)