from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
db = SQLAlchemy(app)
class customers(db.Model):
    id = db.Column('id' , db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer)

    def __repr__(self):
        return f"{self.name} - {self.age}"

def create_db():
    with app.app_context():
        db.create_all()

@app.route('/')
def show_all():
    return render_template('show_all.html',
                           customers=customers.query.all())

if __name__ == '__main__':
    create_db()
    app.run(port=5001, debug=True)

# app = FLASK(__name__)
# db = SQLAlchemy(app)
# class customers(db.Model):
#     id = db.column('id', db.Integer, primary_key=True)
#     name = db.column(db.String(100), nullable=False)
#     age = db.Column(db.Integer)

