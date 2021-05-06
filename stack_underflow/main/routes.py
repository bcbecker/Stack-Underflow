from flask import render_template, request, Blueprint
from stack_underflow.models import Post, Reply

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    # replies = Reply.query.order_by(Reply.date_posted)
    return render_template('index.html', posts=posts)


@main.route("/about")
def about():
    return render_template('about.html', title='About')
