# app.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger

# Initialize the Flask application
app = Flask(__name__)

swagger = Swagger(app)

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
# @app.route('/')
# def hello_world():
#     return 'Hello, World! Our Library API is running.'

# --- API endpoints---
#endpoint to add a new book
@app.route('/books',methods=['POST'])
def add_book():
    """
    Add a new book to the library
    ---
    tags:
      - Books
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            title:
              type: string
              description: The title of the book.
            author:
              type: string
              description: The author of the book.
            published_year:
              type: integer
              description: The year the book was published.
    responses:
      201:
        description: Book created successfully.
    """
    
    data= request.get_json()
    #---Validation---
    if not data or not 'title'in data or not 'author' in data:
        return jsonify({'error': 'Missing required fields: title and author'}), 400
    
    if not data['title'].strip() or not data['author'].strip():
        return jsonify({'error': 'title and author field cannot be empty'}), 400
    #----End validation---
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
    """
    Get a list of all books
    ---
    tags:
      - Books
    responses:
      200:
        description: A list of books.
    """

    # Query the database for all books
    books = Book.query.all()
    # Convert the list of book objects to a list of dictionaries
    book_list = [book.to_dict() for book in books]
    # Return the list as a JSON response
    return jsonify(book_list)

#Endpoint to get a specific book by ID
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    """
    Get a specific book by its ID
    ---
    tags:
      - Books
    parameters:
      - name: book_id
        in: path
        type: integer
        required: true
        description: The ID of the book to retrieve.
    responses:
      200:
        description: The book data.
      404:
        description: Book not found.
    """

    #.get_or_404(book_id) is a handler that will automatically return a 404 not found error if do not exist
    book = Book.query.get_or_404(book_id)
    return jsonify(book.to_dict())

#Endpoint  to delete a book
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):

    """
    Delete a book
    ---
    tags:
      - Books
    parameters:
      - name: book_id
        in: path
        type: integer
        required: true
        description: The ID of the book to delete.
    responses:
      200:
        description: Book deleted successfully.
      404:
        description: Book not found.
    """
    
    book = Book.query.get_or_404(book_id)

    #delete the book fromthe database
    db.session.delete(book)
    db.session.commit()

    #return a sucess message
    return jsonify({'message': 'Book deleted sucessfully'})

# Endpoint to update an existing book
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    """
    Update an existing book
    ---
    tags:
      - Books
    parameters:
      - name: book_id
        in: path
        type: integer
        required: true
        description: The ID of the book to update.
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            title:
              type: string
            author:
              type: string
            published_year:
              type: integer
    responses:
      200:
        description: Book updated successfully.
      404:
        description: Book not found.
    """

    book = Book.query.get_or_404(book_id)
    data = request.get_json()

    #---Validation---
    if not data or not 'title'in data or not 'author' in data:
        return jsonify({'error': 'Missing required fields: title and author'}), 400
    
    if not data['title'].strip() or not data['author'].strip():
        return jsonify({'error': 'title and author field cannot be empty'}), 400
    #----End validation---

    # Update the book's attributes with the new data
    book.title = data['title']
    book.author = data['author']
    book.published_year = data.get('published_year')

    # Commit the changes to the database
    db.session.commit()

    return jsonify(book.to_dict())

#----Error Handlers---
@app.errorhandler(404)
def not_found_error(error):
    return jsonify({'error':'Resource not found'}),404

@app.errorhandler(400)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500


# This allows us to run the app directly from the command line
if __name__ == '__main__':
    app.run(debug=True)