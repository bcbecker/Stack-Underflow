from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from redis import Redis
import rq
from helpme_world.config import Config


db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
mail = Mail()
limiter = Limiter(key_func=get_remote_address,
  default_limits=["200/day", "50/hour"])


def create_app(config_class=Config):
    """
    Binds all necessary objects to app instance, configs with .env
    """
    app = Flask(__name__)
    app.config.from_object(Config)

    app.redis = Redis.from_url(Config.REDIS_URL)
    app.task_queue = rq.Queue('util-tasks', connection=app.redis)

    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    limiter.init_app(app)

    from helpme_world.users.routes import users
    from helpme_world.posts.routes import posts
    from helpme_world.main.routes import main
    from helpme_world.errors.handlers import errors
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app
