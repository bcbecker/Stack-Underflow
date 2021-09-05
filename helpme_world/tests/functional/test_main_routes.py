#flask routes test main.routes.py 

def test_home_route_get(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is requested (GET)
    THEN check that the response is OK (200)
    """
    response = test_client.get('/')
    assert response.status_code == 200

def test_home_route_post(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is requested (POST)
    THEN check that the response is OK (200)
    """
    response = test_client.post('/')
    assert response.status_code == 200

def test_search_route_get(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/search' page is requested (GET)
    THEN check that the response is redirect (302)
    """
    response = test_client.get('/search')
    assert response.status_code == 302

def test_search_route_post(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/search' page is requested (POST)
    THEN check that the response is valid redirect (302)
    """
    response = test_client.post('/search')
    assert response.status_code == 302

def test_about_route_get(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/about' page is requested (GET)
    THEN check that the response is METHOD NOT ALLOWED (405)
    """
    response = test_client.post('/about')
    assert response.status_code == 405

def test_about_route_post(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/about' page is requested (POST)
    THEN check that the response is METHOD NOT ALLOWED (405)
    """
    response = test_client.post('/about')
    assert response.status_code == 405
