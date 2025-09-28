
**OUTPUT: <img width="1755" height="3450" alt="Image" src="https://github.com/user-attachments/assets/46ba3663-2ac6-4b2f-9b96-9d83e84f70ba" />

# Library Management RESTful API 📚

A robust and well-documented RESTful API for managing a collection of books. This project was built to demonstrate the core principles of API development using Python, Flask, and SQLAlchemy.

## Features

  * **Full CRUD Functionality**: Create, Read, Update, and Delete books.
  * **Input Validation**: Ensures required data like `title` and `author` are present and not empty.
  * **JSON Error Handling**: Provides clear, consistent JSON error messages for 404 (Not Found), 400 (Bad Request), and 500 (Internal Server) errors.
  * **Interactive Documentation**: Auto-generated, interactive API documentation powered by Swagger (Flasgger).

-----

## Technology Stack

  * **Backend**: Python 3
  * **Framework**: Flask
  * **ORM**: Flask-SQLAlchemy
  * **Database**: SQLite
  * **API Documentation**: Flasgger (OpenAPI 2.0 / Swagger)

-----

## API Documentation

Interactive API documentation is available once the server is running. It allows you to view all available endpoints and test them directly from your browser.

  * **Swagger UI URL**: `http://127.0.0.1:5000/apidocs`

-----

## ⚙️ Setup and Installation

Follow these steps to get the project running on your local machine.

### 1\. Clone the Repository

```bash
git clone https://github.com/drun16/library-api.git
cd library-api
```

### 2\. Create and Activate a Virtual Environment

It's highly recommended to use a virtual environment to manage project dependencies.

  * **For macOS/Linux:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

  * **For Windows:**

    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```

### 3\. Install Dependencies

Install all the necessary packages from the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

### 4\. Run the Application

This command will start the Flask development server. The `db.create_all()` command will automatically create the `library.db` database file if it doesn't exist.

```bash
python app.py
```

The API will now be running at `http://127.0.0.1:5000`.

-----

## API Endpoints Quick Reference

| Method | Endpoint             | Description                  |
| :----- | :------------------- | :--------------------------- |
| `POST` | `/books`             | Add a new book.              |
| `GET`  | `/books`             | Get a list of all books.     |
| `GET`  | `/books/<book_id>`   | Get a single book by its ID. |
| `PUT`  | `/books/<book_id>`   | Update an existing book.     |
| `DELETE`| `/books/<book_id>`   | Delete a book.               |
