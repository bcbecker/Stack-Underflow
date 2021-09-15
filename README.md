# Helpme_World
helpme_world is a code-centric help forum for developers and hobbyist programmers of all skill levels to come together, collaborate, learn, and assist each other in their programming journeys. It's main focus is bringing posts to users, but it is designed to be scaled up with more helpful features.

To view the live deployment: https://helpme-world.herokuapp.com/home


## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Setup](#setup)
* [Improvements](#improvements)


## General Information
helpme_world is a site meant to serve as a platform for developers and hobbyist programmers to get together to ask questions, communicate ideas, and just enjoy the world of coding. They can make an account, which includes a username, email, and profile picture. Once registered, the user can make posts, reply to other posts, and edit or delete their own posts. The user can also search for posts, or see posts by a specific user.

My purpose for committing to this project is to show a growth mindset. As the project grows, it showcases the growth of my abilities as a back end developer, allowing me to build upon the foundation I've set before myself. The database design, endpoint routing, proper form handling, and error handling are all skills that I've been working to perfect. I felt the Flask framework was an excellent choice for that, because it requires base knowledge of system design to use. Unlike Djnago, Flask is of the "explicit over implicit" mentality, meaning if there is a feature or structure the developer wishes to add/follow, they are in charge of configuring it. Django is much more "batteries included," thus I felt Flask would be a better learning experience.


## Technologies Used
- Flask, including many notable packages
    - WTForms for clean form creation/validation
    - Flask-Login for user management/endpoint authorization
    - Flask-Mail for email service, password reset
    - Bcrypt for password hash checking
    - Jinja2 templating engine
    - SMTP
- SQLAlchemy ORM
- Local SQLite3 and Postgres databases, migrated to Heroku Postgres via S3 bucket
- Bootstrap CSS
- Heroku (for deployment)
- AWS (S3 for db migration)


## Features
- User creation with sha256 password hashing
- User profile picture customization
- Mail server can send password reset email with expiring token
- Users can create update or delete their own posts
- Search by post, view posts by user
- Reply to posts


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

### Creating .env file
For this server to run, you must create a .env file within the package, setting the following parameters:
```bash
SECRET_KEY=
SQLALCHEMY_DATABASE_URI=sqlite:///site.db
EMAIL_USER=
EMAIL_PASS=
```
Set the secret key to whatever you'd like!

### Running the Server

```bash
python run.py
```

### Viewing the website
Site can be found here: http://127.0.0.1:5000/
(for localhost)



## Improvements

Improvements:
- The front end is quite basic, and ideally I'd love to make a React front end
- Upgrade the testing suite, maybe using Selenium for functional testing
- Role guarding pages using @role_required, needs DB refactor

To Do:
- Elasticsearch for full-text searching
- Implement Redis for caching some slow queries ('LIKE', 'COUNT')
- Collapsible navbar for future features

Recently added:
- Rate limiting using Flask-Limiter