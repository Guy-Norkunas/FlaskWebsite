from project import db

class User(db.Model):
    __tablename__ = 'users'

    # Structure of table

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text)
    password = db.Column(db.Text)

    # Getter and Setter?

    def __init__(self, username, password):
        self.username = username
        self.password = password
