#flask routes test posts.routes.py 

def test_new_post_route(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/post/new' page is requested (POST)
    THEN check that the response is redirect (302)
    """
    response = test_client.post('/post/new')
    assert response.status_code == 302

def test_post_route(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/post/1' page is requested (GET)
    THEN check that the response is OK (200)
    """
    response = test_client.get('/post/1')
    assert response.status_code == 200

def test_reply_route(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/post/<int:post_id>/reply' page is requested (POST)
    THEN check that the response is redirect (302)
    """
    response = test_client.get('/post/1/reply')
    assert response.status_code == 302

def test_post_update_route(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/post/<int:post_id>/update' page is requested (POST)
    THEN check that the response is redirect (302)
    """
    response = test_client.post('/post/1/update')
    assert response.status_code == 302
    
def test_post_delete_route(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/post/<int:post_id>/delete' page is requested (POST)
    THEN check that the response is redirect (302)
    """
    response = test_client.post('/post/1/delete')
    assert response.status_code == 302
    