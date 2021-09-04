#models.py untit tests

def test_new_user(new_user):
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check that username, email, and hashed_password fields are defined correctly
    """
    assert new_user.username == "this_is_a_test"
    assert new_user.email == "testemail@email.com"
    assert new_user.password == "secret_stuff"

def test_new_post(new_user, new_post):
    """
    GIVEN a Post model
    WHEN a new Post is created by a user
    THEN check that user_id, title, and content fields are defined correctly
    """
    assert new_post.author == new_user
    assert new_post.title == "This is a test post"
    assert new_post.content == "Super cool post things"

def test_new_reply(new_user, new_post, new_reply):
    """
    GIVEN a Reply model
    WHEN a new Reply is created by a user on a post
    THEN check that user_id and content fields are defined correctly
    """
    assert new_reply.content == "Test reply"
    assert new_reply.reply_author != new_user.id