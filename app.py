# app.py

from flask import Flask

# Initialize the Flask application
app = Flask(__name__)

# Define a route and a view function
@app.route('/')
def hello_world():
    return 'Hello, World! Our Library API is running.'

# This allows us to run the app directly from the command line
if __name__ == '__main__':
    app.run(debug=True)