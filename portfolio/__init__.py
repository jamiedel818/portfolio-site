'''
    The __init__.py file initializes the application.

    This means declaring the app, configuring the database, and setting
    up other tools.

    sqlite database can be imported from portfolio package as 'db'

    bycrypy: used to hash and verify users password
    login_manager: handles user sessions as well as declares the login page
'''
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

#'flask run' in the terminal will run the final version
#'./portfolio will run in degbug mode'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

#So app can see routes.py
#avoids circular imports
from portfolio import routes
