from flask import (render_template,url_for, flash,
                   redirect, request, Blueprint)
from stack_underflow.models import Post, Reply
from stack_underflow.main.forms import SearchForm

main = Blueprint('main', __name__)


@main.route("/", methods=['GET', 'POST'])
@main.route("/home", methods=['GET', 'POST'])
def home():
    form = SearchForm()
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('index.html', posts=posts, form=form, legend='Search Posts')

@main.route("/search", methods=['GET', 'POST'])
def search():
    form = SearchForm()
    page = request.args.get('page', 1, type=int)
   
    if form.validate_on_submit():
        keyword = form.keyword.data
        search = "%{}%".format(keyword)
        posts = Post.query.filter(Post.title.like(search)).paginate(page=page, per_page=5)
        return render_template('index.html', posts=posts, form=form, legend='Search Posts')

    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return redirect(url_for('main.home', posts=posts, form=form, legend='Search Posts'))

@main.route("/about")
def about():
    return render_template('about.html', title='About')
