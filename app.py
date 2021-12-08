"""Blogly application."""

from flask import Flask, request, redirect, render_template, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User, Post, Tag, PostTag


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()

@app.route('/')
def root():
    """Homepage redirects to list of users."""

    return redirect("/users")

@app.route('/users')
def show_users():
    '''Show all users'''

    users = User.query.order_by(User.last_name, User.first_name)
    return render_template('users/index.html', users=users)

@app.route('/users/new', methods = ["GET"])
def add_user_get():
    '''Show an add form for users'''

    return render_template('users/new.html')

@app.route('/users/new', methods = ["POST"])
def add_user():
    '''Processing add form, adding a new user and going back to /users'''

    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    image_url = request.form["image_url"] or None

    new_user = User(first_name = first_name, last_name = last_name, image_url = image_url)

    db.session.add(new_user)
    db.session.commit()

    return redirect('/users')

@app.route('/users/<int:user_id>')
def show_user(user_id):
    '''Show a page info with a specific user'''

    user = User.query.get_or_404(user_id)
    return render_template('users/show.html', user=user)

@app.route('/users/<int:user_id>/edit', methods=["GET"])
def show_edit(user_id):
    '''Show edit page for user'''

    user = User.query.get_or_404(user_id)
    return render_template('users/edit.html', user=user)

@app.route('/users/<int:user_id>/edit', methods=["POST"])
def process_edit(user_id):
    '''Process the edit form and return the user back to the /users page'''

    user = User.query.get_or_404(user_id)
    
    user.first_name = request.form["first_name"]
    user.last_name = request.form["last_name"]
    user.image_url = request.form["image_url"] 

    db.session.add(user)
    db.session.commit()

    return redirect('/users')

@app.route('/users/<int:user_id>/delete', methods=["POST"])
def delete_user(user_id):
    '''Delete user'''

    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()

    return redirect('/users')

###############################################################################################################################
# Post Route

@app.route('/users/<int:user_id>/posts/new')
def post_form(user_id):
    '''Show form to add post for that user'''

    user = User.query.get_or_404(user_id)
    return render_template('posts/new.html', user=user)

@app.route('/users/<int:user_id>/posts/new', methods = ["POST"])
def process_post(user_id):
    '''Handle add form, add post and redirect to the user detail page'''

    user = User.query.get_or_404(user_id)
    title = request.form["title"]
    content = request.form["content"]
    
    new_post = Post(title=title, content=content, user=user)
    db.session.add(new_post)
    db.session.commit()

    # flash(f'Post {new_post.title} added.')

    return redirect(f'/users/{user_id}')

@app.route('/posts/<int:post_id>')
def show_post(post_id):
    '''Show a post'''

    post = Post.query.get_or_404(post_id)
    return render_template('posts/show.html', post=post)

@app.route('/posts/<int:post_id>/edit')
def edit_post(post_id):
    '''Show form to edit post'''

    post = Post.query.get_or_404(post_id)
    return render_template('posts/edit.html', post=post)

@app.route('/posts/<int:post_id>/edit', methods=['POST'])
def handle_edit_post(post_id):
    '''Handle editing a post, redirect back to post view'''

    post = Post.query.get_or_404(post_id)

    post.title = request.form["title"]
    post.content = request.form["content"]

    db.session.add(post)
    db.commit()

    return redirect(f'/users/{post.user_id}')

@app.route('/posts/<int:post_id>/delete', methods = ["POST"])
def delete_post(post_id):
    '''Delete post'''

    post = Post.query.get_or_404(post_id)

    db.session.delete(post)
    db.session.commit()

    return redirect(f'/users/{post.user_id}')


###############################################################################################################################
#Tag Route

@app.route('/tags')
def get_tags():
    '''List all tags'''

    tags = Tag.query.all()
    return render_template('tags/index.html', tags=tags)

@app.route('/tags/<int:tag_id>')
def tag_detail(tag_id):
    '''Show details about a tag'''

    tag = Tag.query.get_or_404(tag_id)

    return render_template('tags/show.html', tag=tag)

@app.route('/tags/new')
def new_tag():
    '''Show form to add new tag'''

    return render_template('tags/new.html')

@app.route('/tags/new', methods = ["POST"])
def process_new_tag():
    '''Process add form, add tag, redirect to tag list'''
    
    new_tag = Tag(name=request.form["name"])
    db.session.add(new_tag)
    db.session.commit()

    return redirect('/tags')






