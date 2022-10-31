"""Models for Blogly."""
from cgi import print_form
from flask_sqlalchemy import SQLAlchemy
import datetime
db = SQLAlchemy()


def connect_db(app):
    db.app = app
    db.init_app(app)



class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)

    first_name = db.Column(db.String(20), nullable = False)

    last_name = db.Column(db.String(20), nullable = False)

    image_url = db.Column(db.String)


class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)

    title = db.Column(db.String, nullable = False)

    content = db.Column(db.String, nullable = False)

    created_at = db.Column(db.DateTime, default = datetime.datetime.now)

    userId = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)

    user = db.relationship('User')


class Tag_Post(db.Model):
    __tablename__ = 'tag_post'

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)

    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable = False, primary_key = True)

    tag_id = db.Column(db.Integer, db.ForeignKey('tags.id'), nullable = False, primary_key = True)


class Tag(db.Model):
    __tablename__ = 'tags'

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)

    tag_name = db.Column(db.String, nullable = False, unique = True)

    posts = db.relationship('Post', secondary = 'tag_post', backref = 'tags')



