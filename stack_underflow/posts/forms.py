from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    """
    Collects title and content for submitting new post
    """
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')

class ReplyForm(FlaskForm):
    """
    Collects content for submitting a reply to a post
    """
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Reply')
