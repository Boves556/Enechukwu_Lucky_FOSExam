# First we import flask and SQLAlchemy from flask and flask_sqlalchemy respectively
from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# We Initialize the Flask application and configure the part for the SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'


# after that we create a SQLAlchemy object to handle the database
db = SQLAlchemy(app)

# Then we define the Book model with id, title, author, and publication year
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    author = db.Column(db.String(80), nullable=False)
    publication_year = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Book {self.title}>'

# Then we create the routes
@app.route('/books')
def list_books():
    books = Book.query.all()
    return render_template('books.html', books=books)

@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        new_book = Book(
            title=request.form['title'],
            author=request.form['author'],
            publication_year=request.form['publication_year']
        )

        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('list_books'))
    # We render the add_book template if the method is GET
    return render_template('add_book.html')

# We write a function to create the database tables within the application
def add_context():
    with app.app_context():
        db.create_all()

# After that we run the Flask app
if __name__ == '__main__':
    add_context()  # Create database tables
    app.run(port=5001, debug=True)
