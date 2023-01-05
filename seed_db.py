import os
import crud
import model
from model import db, connect_to_db, User, Book, Users_book
import server

os.system("dropdb books")
os.system("createdb books")

model.connect_to_db(server.app)
model.db.create_all()


user1 = User("user1@test.com", "test", "ted", "d")
user2 = User("user2@test.com", "test", "sue", "f")
user3 = User("user3@test.com", "test", "bob", "b")
user4 = User("user4@test.com", "test", "guy", "q")
user5 = User("user5@test.com", "test", "hillary", "t")
user6 = User("user6@test.com", "test", "toni", "c")
user7 = User("user7@test.com", "test", "brad", "o")

model.db.session.add_all([user1, user2, user3, user4, user5, user6, user7])
model.db.session.commit()

book1 = Book("The Brothers Karamazov", "Fyodor Dostoevsky", 840, "blah", "default.jpg")
book2 = Book("The Crossing", "Cormac McCarthy", 425, "blah", "default.jpg")
book3 = Book("Anna Karenina", "Leo Tolstoy", 864, "blah", "default.jpg")
book4 = Book("The Count of Monte Cristo", "Alexandre Dumas", 1152, "blah", "default.jpg")
book5 = Book("The Magic Mountain", "Thomas Mann", 720, "blah", "default.jpg")
book6 = Book("One Hundred Years of Solitude", "Gabriel Garcia Marquez", 417, "blah", "default.jpg")
book7 = Book("In Cold Blood", "Truman Capote", 432, "blah", "default.jpg")
book8 = Book("The Death Ship", "B. Traven", 384, "blah", "default.jpg")

model.db.session.add_all([book1, book2, book3, book4, book5, book6, book7, book8])
model.db.session.commit()

# user_book1 = Users_book(0, 0, 25, True)

# model.db.session.add(user_book1)
# model.db.session.commit()

# for x in range(10):
#     email = f"user{x}@test.com"
#     password = "test"


#     user = crud.create_user(email, password)
#     model.db.session.add(user)

# if __name__ == "__main__":
#     from server import app
#     connect_to_db(app)
