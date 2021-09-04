# Helpme_World
This is a larger-scale Flask server with user authentication, using a PostgreSQL database with SQLAlchemy as an ORM. The front end consists of Jinja2 templating, and Bootstrap CSS.


## Setup

Ensure python 3.9 is installed.

Install requirements:
```bash
pip install -r requirements.txt
```

Or, access virtual environment:
```bash
pip install pipenv
pipenv shell
```

## Creating .env file

For this server to run, you must create a .env file within the package, setting the following paramters:
```bash
SECRET_KEY=
SQLALCHEMY_DATABASE_URI=sqlite:///site.db
EMAIL_USER=
EMAIL_PASS=
```
Set the secret key to whatever you'd like!

## Running the Server

```bash
python run.py
```

## Viewing the website

Site can be found here: http://127.0.0.1:5000/
(for localhost)


## Navigating the site

helpme_world is a site meant to serve as a platform for developers and hobbyist programmers to get together to ask questions, communicate ideas, and just enjoy the world of coding. They can make an account, which includes a username and a distinct user picture, which is hashed and uploaded to the database. Once registered, there is a token in place to reset a user's password, if needed. The user can make posts, reply to other posts, and see posts made by a specific user. New features will be added to the sidebar to increase user resources. 
