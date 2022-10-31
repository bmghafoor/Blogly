"""Seed file to make sample data for users posts db."""

from app import app
from models import User, Post, Tag, db


with app.app_context():
    # Create all tables
    db.drop_all()
    db.create_all()

    # If table isn't empty, empty it
    User.query.delete()
    Post.query.delete()

    # Add users
    John = User(first_name='John', last_name='Doe', image_url="image here")
    Jacob = User(first_name='Jacob', last_name='Jones', image_url="image here")


    # Add new objects to session, so they'll persist
    db.session.add(John)
    db.session.add(Jacob)

    db.session.commit()

    # Add tables
    post1 = Post(title='Chopsticks are cool', content = 'Forks are way better so are sporks', userId = 1)
    post2 = Post(title='Chopsticks are cool', content = 'Forks are way better so are sporks', userId = 2)

    db.session.add(post1)
    db.session.add(post2)

    db.session.commit()


    # Add in tags

    Fun = Tag(tag_name='Fun')
    Truth = Tag(tag_name='Truth')

    db.session.add(Fun)
    db.session.add(Truth)

    db.session.commit()
    

