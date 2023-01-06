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

book1 = Book("The Brothers Karamazov", "Fyodor Dostoevsky", 840, "blah", "https://kbimages1-a.akamaihd.net/561f9624-ba0a-43dc-a569-dac6327e3804/1200/1200/False/the-brothers-karamazov-233.jpg")
book2 = Book("The Crossing", "Cormac McCarthy", 425, "blah", "http://prodimage.images-bn.com/pimages/9780679760849_p0_v3_s1200x630.jpg")
book3 = Book("Anna Karenina", "Leo Tolstoy", 864, "blah", "http://4.bp.blogspot.com/-TuW3ThIlOVo/T56rSQq9wcI/AAAAAAAAEvM/3LfEYFQkqXI/s1600/anna-karenina.jpg")
book4 = Book("The Count of Monte Cristo", "Alexandre Dumas", 1152, "blah", "https://cdnb.artstation.com/p/assets/images/images/026/842/803/large/suze-gil-count-of-monte-cristo.jpg?1589886873")
book5 = Book("The Magic Mountain", "Thomas Mann", 720, "blah", "https://covers.openlibrary.org/b/id/7392177-L.jpg")
book6 = Book("One Hundred Years of Solitude", "Gabriel Garcia Marquez", 417, "blah", "https://dwcp78yw3i6ob.cloudfront.net/wp-content/uploads/2016/12/12162813/100_Years_First_Ed_Hi_Res-768x1153.jpg")
book7 = Book("In Cold Blood", "Truman Capote", 432, "blah", "https://thebooklyclub.files.wordpress.com/2015/01/capote.jpg")
book8 = Book("The Death Ship", "B. Traven", 384, "blah", "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1350392572l/2104716.jpg")

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
