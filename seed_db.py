import os
import json
import crud
import model
import server

os.system("dropdb books")
os.system("createdb books")

model.connect_to_db(server.app)
model.db.drop_all()
model.db.create_all()

with open('data/books.json') as f:
        book_data = json.loads(f.read())

books_in_db = []

for book in book_data:
    title = book["title"]
    author = book["author"]
    length = book["length"]
    overview = book["overview"]

    db_book = crud.create_book(title, author, length, overview)
    books_in_db.append(db_book)

model.db.session.add_all(books_in_db)
model.db.session.commit()

for x in range(10):
    email = f"user{x}@test.com"
    password = "test"

    user = crud.create_user(email, password)
    model.db.session.add(user)