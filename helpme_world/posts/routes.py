from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from helpme_world import db
from helpme_world.models import Post, Reply
from helpme_world.posts.forms import PostForm, ReplyForm

posts = Blueprint('posts', __name__)


@posts.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
    """
    If the form validates, commits new post data to db
    """
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_post.html', title='New Post',
                           form=form, legend='New Post')


@posts.route("/post/<int:post_id>", methods=['GET'])
def post(post_id):
    """
    Gets/renders post by id, or returns 404
    """
    form = ReplyForm()
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, form=form, post=post)


@posts.route("/post/<int:post_id>/reply", methods=['GET', 'POST'])
@login_required
def new_reply(post_id):
    """
    If form validates, commits reply data to db
    """
    post = Post.query.get_or_404(post_id)
    form = ReplyForm()
    if form.validate_on_submit():
        reply = Reply(content=form.content.data, reply_author=current_user, post_id=post.id)
        db.session.add(reply)
        db.session.commit()
        flash('Your reply has been posted!', 'success')
        return redirect(url_for('posts.post', post_id=post.id))
    return render_template('post.html', title='Reply Post',
                           form=form, post=post, legend='Reply Post')


@posts.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    """
    Updates post data to db if post exists and author is current_user
    """
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('posts.post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('create_post.html', title='Update Post',
                           form=form, legend='Update Post')


@posts.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    """
    Deletes post data from db if user is current_user
    """
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('main.home'))
