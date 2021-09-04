#unit test fixtures
import pytest
from helpme_world.models import User, Post, Reply


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