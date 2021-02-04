from flask import Flask
from flask_mysqldb import MySQL
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'guy'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'test'

mysql = MySQL(app)

@app.route('/')
def hello_world():
    cur = mysql.connection.cursor()
    cur.execute("SELECT string FROM test;")
    return(str(cur.fetchall()))


## test