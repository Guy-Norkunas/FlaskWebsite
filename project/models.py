from project import db

class User(db.Model):
    __tablename__ = 'users'

    # Structure of table

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))

    # Getter and Setter?

    def __init__(self, username, password):
        self.username = username
        self.password = password
