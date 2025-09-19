from flask import Flask, request
app - Flask (__name__)
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(80), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    publisher = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f"{self.book_name} - {self.description}"

@app.route('/')
def index():
    return "Hello"

@app.route('/Book')
def get_book():
    book = Book.query.all()
    output = []
    for b in book:
        book_data = {'name' : b.book_name, 'author': book.author }
    return{"id": "book_name", "author", "publisher"}

@app.route('/book/<id>')
def book(id): 
    book = Book.query.get_or_404(id)
    return {"name": book.book_name, "author": book.author, "publisher": book.publisher}

@app.route('/book', methods=['POST'])
def add_book():
    book = Book(book_name=request.json['book_name'], author=request.json['author'], publisher=request.json['publisher'])
    db.session.add(book)
    db.session.commit()
    return {'id': book.id}

app.route('/book/<id>', methods=['DELETE'])
def delete_book():
    book = Book.query.get(id)
    if book is None:
        return {"error": "not found"}
    db.session.delete(book)
    db.session.commit()
    return {"message": "yeet!"}
    