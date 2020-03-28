'''
    Contains the database model that represents the websites users.

    login_manager decorater builds off the login manager object from __init__
        -Allows us to use the load_user function
        -UserMixin inherits from class and gives us user methods

    __repr__ delclares how users will be returned within the database
'''
from portfolio import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return user.query.get(int(user_id))

class user(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(30), unique=True, nullable=False)

    def __repr__(self):
        return f"User('{self.id}', '{self.username}', '{self.email}')"
