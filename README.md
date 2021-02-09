# FlaskWebsite

## How to run
#
### 1. Clone project to your local machine
```
git clone https://github.com/Guy-Norkunas/FlaskWebsite
```
#
### 2. Install dependencies

```
pipenv install
```
#
### 3. Add some variables to environment

- Get API_KEY from https://www.themoviedb.org/
- DATABASE_URI is in the form [db]://[user]:[password]@[host]:[port]/[dbname] eg. mysql://root:pass@localhost/test
- SECRET_KEY is used for encryption

```
export API_KEY=""
export DATABASE_URI=""
export SECRET_KEY=""
```
#
### 4.1 Setting up database

run these commands to set up your database

```
flask db init
flask db migrate
flask db upgrade
```
### 4.2 Alternative

if that doesn't work create a users table and movies table in your database. give users a username columnn and password column, both of type VARCHAR(100). then give the movies table a movie_id column and user_id column, these are both of type INT.

#
### 5. You're ready to run the server

```
flask run
```

- Open a webrowser and go to http://localhost:5000 and you should see the homepage of the website
