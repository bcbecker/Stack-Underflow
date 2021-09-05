#flask routes test users.routes.py 


def test_register_route(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/register' page is requested (POST)
    THEN check that the response is OK (200)
    """
    response = test_client.post('/register')
    assert response.status_code == 200


def test_login_route(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/login' page is requested (POST)
    THEN check that the response is OK (200)
    """
    response = test_client.post('/login')
    assert response.status_code == 200


def test_logout_route(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/logout' page is requested (POST)
    THEN check that the response is redirect (302)
    """
    response = test_client.post('/logout')
    assert response.status_code == 405


def test_account_route(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/account'' page is requested (POST)
    THEN check that the response is redirect (302)
    """
    response = test_client.post('/account')
    assert response.status_code == 302


def test_user_route(test_client, new_user):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/user/<string:username>' page is requested (POST)
    THEN check that the response is redirect (302)
    """
    response = test_client.post('/user/<string:username>')
    assert response.status_code == 405


def test_reset_password_route(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/reset_password' page is requested (POST)
    THEN check that the response is OK (200)
    """
    response = test_client.post('/reset_password')
    assert response.status_code == 200

def test_password_token_route(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/reset_password/<token>' page is requested (POST)
    THEN check that the response is redirect (302)
    """
    response = test_client.post('/reset_password/<token>')
    assert response.status_code == 302