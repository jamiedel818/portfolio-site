'''
    Defines all the forms used in the website:
        -registration
        -login
'''
from flask_wtf import FlaskForm
from portfolio.dbModel import user
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

'''
    Represents the user registration form
    Custom Validators:
        validate_username: ensures usernames are unique in the database
        validate_password: ensures passwords are unique in the database
'''
class registerForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirmPassword = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])

    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        newUser = user.query.filter_by(username=username.data).first()
        if newUser:
            raise ValidationError('Username already exists! Please choose another.')

    def validate_email(self, email):
        newUser = user.query.filter_by(email=email.data).first()
        if newUser:
            raise ValidationError('Email already exists! Please choose another.')

'''
    Represents the user login form
'''
class loginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    rememberMe = BooleanField('Remember Me')

    submit = SubmitField('Login')
