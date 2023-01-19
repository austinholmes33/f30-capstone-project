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

book1 = Book("The Brothers Karamazov", "Fyodor Dostoevsky", 840, "Set in 19th-century Russia, The Brothers Karamazov is a passionate philosophical novel that enters deeply into questions of God, free will, and morality.", "https://kbimages1-a.akamaihd.net/561f9624-ba0a-43dc-a569-dac6327e3804/1200/1200/False/the-brothers-karamazov-233.jpg")
book2 = Book("The Crossing", "Cormac McCarthy", 425, "Cormac McCarthy's The Crossing is a 1994 coming-of-age Western that explores humanity's relationship with the frontier through teenager Billy Parham's journeys during the early 1940s", "http://prodimage.images-bn.com/pimages/9780679760849_p0_v3_s1200x630.jpg")
book3 = Book("Anna Karenina", "Leo Tolstoy", 864, "A complex novel in eight parts. It deals with themes of betrayal, faith, family, marriage, Imperial Russian society, desire, and rural vs. city life. The story centers on an extramarital affair between Anna and dashing cavalry officer Count Alexei Kirillovich Vronsky.", "http://4.bp.blogspot.com/-TuW3ThIlOVo/T56rSQq9wcI/AAAAAAAAEvM/3LfEYFQkqXI/s1600/anna-karenina.jpg")
book4 = Book("The Count of Monte Cristo", "Alexandre Dumas", 1152, "An adventure story centrally concerned with themes of hope, justice, vengeance, mercy, and forgiveness. It centers on a man who is wrongfully imprisoned, escapes from jail, acquires a fortune, and sets about exacting revenge on those responsible for his imprisonment.", "https://cdnb.artstation.com/p/assets/images/images/026/842/803/large/suze-gil-count-of-monte-cristo.jpg?1589886873")
book5 = Book("The Magic Mountain", "Thomas Mann", 720, "A novel by Thomas Mann, first published in German in November 1924. It is widely considered to be one of the most influential works of twentieth-century German literature.", "https://covers.openlibrary.org/b/id/7392177-L.jpg")
book6 = Book("One Hundred Years of Solitude", "Gabriel Garcia Marquez", 417, "Considered García Márquez's magnum opus, remains widely acclaimed and is recognized as one of the most significant works both in the Hispanic literary canon[10] and in world literature.", "https://dwcp78yw3i6ob.cloudfront.net/wp-content/uploads/2016/12/12162813/100_Years_First_Ed_Hi_Res-768x1153.jpg")
book7 = Book("In Cold Blood", "Truman Capote", 432, "A non-fiction novel[1] by American author Truman Capote, first published in 1966. It details the 1959 murders of four members of the Clutter family in the small farming community of Holcomb, Kansas.", "https://thebooklyclub.files.wordpress.com/2015/01/capote.jpg")
book8 = Book("The Death Ship", "B. Traven", 384, "A novel by the pseudonymous author known as B. Traven. Originally published in German in 1926, and in English in 1934, it was Traven's first major success and is still the author's second best known work after The Treasure of the Sierra Madre. Owing to its scathing criticism of bureaucratic authority, nationalism, and abusive labor practices, it is often described as an anarchist novel.", "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1350392572l/2104716.jpg")

model.db.session.add_all([book1, book2, book3, book4, book5, book6, book7, book8])
model.db.session.commit()

user_book1 = Users_book(1, 1, 25, True)
user_book2 = Users_book(1, 2, 57, True)
user_book3 = Users_book(1, 3, 0, False)
user_book4 = Users_book(1, 4, 0, False)
user_book5 = Users_book(1, 5, 0, False)
user_book6 = Users_book(1, 6, 0, False)
user_book7 = Users_book(1, 7, 11, True)
user_book8 = Users_book(1, 8, 0, False)


model.db.session.add_all([user_book1, user_book2, user_book3, user_book4, user_book5, user_book6, user_book7, user_book8])
model.db.session.commit()

# for x in range(10):
#     email = f"user{x}@test.com"
#     password = "test"


#     user = crud.create_user(email, password)
#     model.db.session.add(user)

# if __name__ == "__main__":
#     from server import app
#     connect_to_db(app)
