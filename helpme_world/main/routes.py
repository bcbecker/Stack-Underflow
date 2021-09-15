from flask import (render_template, url_for,
                   redirect, request, Blueprint)
from helpme_world import limiter
from helpme_world.models import Post
from helpme_world.main.forms import SearchForm

main = Blueprint('main', __name__)


@main.route("/", methods=['GET', 'POST'])
@main.route("/home", methods=['GET', 'POST'])
@limiter.limit("1/second", override_defaults=False)
def home():
    """
    Fetches all posts(paginated), and top posts
    """
    form = SearchForm()
    page = request.args.get('page', 1, type=int)
    top_posts = Post.get_top_posts()
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('index.html', posts=posts, top_posts=top_posts, form=form, legend='Search Posts')

@main.route("/search", methods=['POST'])
@limiter.limit("1/second", override_defaults=False)
def search():
    """
    Fetches searched-for posts (paginated), and top posts
    """
    form = SearchForm()
    page = request.args.get('page', 1, type=int)
    top_posts = Post.get_top_posts()
    if form.validate_on_submit():
        keyword = form.keyword.data
        search = "%{}%".format(keyword)
        posts = Post.query.filter(Post.title.like(search)).paginate(page=page, per_page=5)
        return render_template('index.html', posts=posts, form=form, legend='Search Posts')

    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return redirect(url_for('main.home', posts=posts, top_posts=top_posts, form=form, legend='Search Posts'))

@main.route("/about")
@limiter.limit("1/second", override_defaults=False)
def about():
    """
    Renders the about page
    """
    return render_template('about.html', title='About')
