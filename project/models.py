from project import db
from flask_login import UserMixin

# users table

class User(UserMixin, db.Model):
    __tablename__ = 'users'

    # Structure of table

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))

    # Getter and Setter?

    def __init__(self, username, password):
        self.username = username
        self.password = password

# movies table

class Movies(db.Model):
    __tablename__ = 'movies'

    # Structure of table

    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer)

    # Getter and Setter

    def __init__(self, movie_id, user_id):
        self.movie_id = movie_id
        self.user_id = user_id