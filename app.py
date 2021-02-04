from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://guy:password@localhost/test'
db = SQLAlchemy(app)

@app.route('/')
def hello_world():
    
    return("hello there")