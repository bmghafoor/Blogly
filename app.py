"""Blogly application."""

from operator import methodcaller
from flask import Flask, request, redirect, render_template
from models import db, connect_db, User, Post, Tag, Tag_Post

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)


@app.route("/")
def show_users():
    """List Users"""
    users = User.query.all()
    return render_template("base.html",users=users)




@app.route("/", methods=["POST"])
def add_user():
    """Add user and redirect to list."""

    first_name = request.form['firstname']
    last_name = request.form['lastname']
    image_url = request.form['imageurl']
    user = User(first_name=first_name, last_name=last_name, image_url=image_url)
    db.session.add(user)
    db.session.commit()
    return redirect("/")




@app.route("/users/new")
def add_user_form():
    """Show form for new user"""
    return render_template('new_user.html')






@app.route("/<int:user_id>")
def show_user_info(user_id):
    """Show info on a single user."""
    user = User.query.get_or_404(user_id)
    posts = Post.query.filter_by(userId = user_id).all()
    return render_template("user_detail.html", user=user, posts=posts)





@app.route("/<int:user_id>/edit")
def edit_user(user_id):
    """Edit info on a single user."""
    user = User.query.get_or_404(user_id)
    return render_template("user_edit.html", user=user)




@app.route("/users/<int:user_id>/edit", methods=["POST"])
def update_user(user_id):
    """Add user and redirect to list."""
    user = User.query.get_or_404(user_id)
    user.first_name = request.form['firstname']
    user.last_name = request.form['lastname']
    user.image_url = request.form['imageurl']
    db.session.add(user)
    db.session.commit()
    return redirect("/")



@app.route("/user/<int:user_id>/delete", methods=["POST"])
def delete_user(user_id):
    """Add user and redirect to list."""
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return redirect("/")



    # ----------------------------------------------- Part 2 ----------------------------------------------
    
@app.route('/<int:user_id>/add_post')
def add_post(user_id):
    """Add a new post"""
    user = User.query.get_or_404(user_id)
    tags = Tag.query.all()

    return render_template('new_post.html', user=user, tags=tags)



@app.route('/<int:user_id>/add_post', methods = ['POST']) 
def create_post(user_id):
    """Add a new post"""

    user = User.query.get_or_404(user_id)

    title = request.form['title']
    content = request.form['content']

    tag_ids = [int(num) for num in request.form.getlist("tags")]
    tags = Tag.query.filter(Tag.id.in_(tag_ids)).all()
    
    new_post = Post(title=title, content=content, userId=user.id, tags=tags)



    db.session.add(new_post)
    db.session.commit()
    return redirect("/")


@app.route('/post/<int:post_id>/')
def view_post(post_id):
    """Return Info on Post"""
    post = Post.query.get_or_404(post_id)

    return render_template('post_detail.html', post=post)



@app.route('/post/<int:post_id>/edit')
def edit_post(post_id):
    """Return Edit Page on Post"""
    post = Post.query.get_or_404(post_id)
    tags = Tag.query.all()

    return render_template('post_edit.html',post=post, tags = tags)



@app.route('/post/<int:post_id>/edit', methods=['POST'])
def update_post(post_id):
    """Edit Post"""

    post = Post.query.get_or_404(post_id)
    post.title = request.form['title']
    post.content = request.form['content']

    tag_ids = [int(num) for num in request.form.getlist("tags")]
    post.tags = Tag.query.filter(Tag.id.in_(tag_ids)).all()

    db.session.add(post)
    db.session.commit()

    return redirect('/')


@app.route('/post/<int:post_id>/delete', methods = ['POST'])
def del_post(post_id):
    """Return Info on Post"""
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()

    return redirect('/') 


# -------------------------------------------------------------- Part 3 ------------------------------------------------------------- 

@app.route('/tags')
def show_tags():
    """Show tags"""

    tags = Tag.query.all()
    return render_template('tags.html',tags=tags)


@app.route('/tags', methods=['POST'])
def add_tag():
    """Add tag"""

    tagname = request.form['tagname']
    tag = Tag(tag_name = tagname)
    db.session.add(tag)
    db.session.commit()

    return redirect ('/tags')


@app.route('/tag/<int:tag_id>/delete', methods = ['POST'])
def delete_tag(tag_id):
    """Delete a Tag"""

    tag = Tag.query.get_or_404(tag_id)
    db.session.delete(tag)
    db.session.commit()

    return redirect ('/tags')



@app.route('/tags/<int:tag_id>')
def show_tag(tag_id):
    """Show information on one specifc tag"""

    tag = Tag.query.get_or_404(tag_id)
    return render_template('tag.html', tag=tag)




@app.route('/tags/new')
def tag_new():
    """Template for adding new Tag"""

    return render_template('tags_new.html')



@app.route('/tags/<int:tag_id>/edit')
def tag_edit(tag_id):
    """Return Tag Edit Page"""

    tag = Tag.query.get_or_404(tag_id)

    return render_template ('tag_edit.html', tag=tag)


@app.route('/tag/<int:tag_id>/edit', methods = ['POST'])
def edit_tag(tag_id):
    """Post new info on editing a tag"""

    tag = Tag.query.get_or_404(tag_id)
    tag.tag_name = request.form['tagname']
    db.session.add(tag)
    db.session.commit()

    return redirect ('/tags')











