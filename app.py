# app.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)

#__Database Configuration ___
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = False)
    author = db.Column(db.String(100), nullable = False)
    published_year = db.Column(db.Integer)

    def to_dict(self):
        return {
            'id' : self.id,
            'title' : self.title,
            'author' : self.author,
            'published_year' : self.published_year
        }

# Define a route and a view function
@app.route('/')
def hello_world():
    return 'Hello, World! Our Library API is running.'

# --- API endpoints---
#endpoint to add a new book
@app.route('/books',methods=['POST'])
def add_book():

    data= request.get_json()

    new_book = Book(
        title = data['title'],
        author = data['author'],
        published_year = data.get('published_year')
    )

    db.session.add(new_book)
    db.session.commit()

    return jsonify(new_book.to_dict()), 201

#Endpoint to get all books
@app.route('/books', methods=['GET'])
def get_all_books():
    # Query the database for all books
    books = Book.query.all()
    # Convert the list of book objects to a list of dictionaries
    book_list = [book.to_dict() for book in books]
    # Return the list as a JSON response
    return jsonify(book_list)

# This allows us to run the app directly from the command line
if __name__ == '__main__':
    app.run(debug=True)