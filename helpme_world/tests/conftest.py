#unit test fixtures
import pytest
from helpme_world.models import User, Post, Reply
from helpme_world import create_app
from helpme_world.config import Config


@pytest.fixture()
def test_client():
    """
    Create test app with proper config
    """
    app = create_app()
    app.config['TESTING'] = True
    app.config['SECRET_KEY'] = Config.SECRET_KEY
    app.config['SQLALCHEMY_DATABASE_URI'] = Config.SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = Config.SQLALCHEMY_TRACK_MODIFICATIONS
    app.config['DEBUG'] = False

    with app.test_client() as test_client:
        with app.app_context():
            yield test_client

@pytest.fixture()
def new_user():
    """
    Create user for testing
    """
    user = User(username="this_is_a_test", email="testemail@email.com", password="secret_stuff")
    return user

@pytest.fixture()
def new_post():
    """
    Create user and post for testing
    """
    user = User(username="this_is_a_test", email="testemail@email.com", password="secret_stuff")
    post = Post(title="This is a test post", content="Super cool post things", author=user)
    return post

@pytest.fixture()
def new_reply():
    """
    Create two user, post, and reply for testing
    """
    user = User(username="this_is_a_test", email="testemail@email.com", password="secret_stuff")
    user2 = User(username="this_is_a_test_replier", email="test_reply_email@email.com", password="secreter_stuff")
    post = Post(title="This is a test post", content="Super cool post things", author=user)
    reply = Reply(content="Test reply", reply_author=user2, post_id=post)
    return reply