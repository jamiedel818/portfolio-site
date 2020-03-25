from flask import Flask
from flask_sqlalchemy import SQLAlchemy



#'flask run' in the terminal will run the final version
#'./portfolio will run in degbug mode'
app = Flask(__name__)
app.config['SECRET_KEY'] = '2b403c1b27dcef0398450657a46ef027'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

#So app can see the routes
#avoides circular imports
from portfolio import routes
