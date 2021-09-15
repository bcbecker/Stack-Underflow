from flask import Blueprint, render_template

errors = Blueprint('errors', __name__)


@errors.app_errorhandler(404)
def error_404(error):
    """
    Renders 404 template upon 404 error
    """
    return render_template('errors/404.html'), 404


@errors.app_errorhandler(403)
def error_403(error):
    """
    Renders 403 template upon 403 error
    """
    return render_template('errors/403.html'), 403

@errors.app_errorhandler(429)
def error_429(error):
    """
    Renders 429 template upon 429 error
    """
    return render_template('errors/429.html'), 429

@errors.app_errorhandler(500)
def error_500(error):
    """
    Renders 500 template upon 500 error
    """
    return render_template('errors/500.html'), 500
