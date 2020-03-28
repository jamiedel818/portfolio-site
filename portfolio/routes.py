'''
    Defines routes for all pages on the website
    Handles user authentication and user session info
'''
from flask import render_template, url_for, flash, redirect, request
from portfolio import app, db, bcrypt
from portfolio.forms import registerForm, loginForm
from portfolio.dbModel import user
from portfolio.getRepos import handleData
from flask_login import login_user, logout_user, current_user, login_required

'''
    Homepage Route:
        -Grabs projects from github
        -Renders home template
'''
@app.route('/')
@app.route('/home')
def home():
    projects = handleData()
    return render_template('home.html', projects=projects, title="Home")

'''
    About Route:
        -Renders about page template
'''
@app.route('/about')
def about():
    return render_template('about.html', title='About')

'''
    Registration page route:
        -Redirects to homepage if user is alread logged in
        -Handles user registration
        -Hashes users passwords
        -Commits new user to the database
'''
@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = registerForm()
    if form.validate_on_submit():
        hashedPwd = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        newUser = user(username=form.username.data, email=form.email.data, password=hashedPwd)
        db.session.add(newUser)
        db.session.commit()
        flash(f'Account created for {form.username.data}! You are now able to login', 'success')
        return redirect(url_for('login'))

    return render_template('register.html', title='Register', form=form)

'''
    Login Page Route:
        -Redirects to homepage if user is alread logged in
        -Queries the database for matching email and checks input
            password vs stored hashed password
        -Handles bad login
'''
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = loginForm()
    if form.validate_on_submit():
        newUser = user.query.filter_by(email=form.email.data).first()
        if newUser and bcrypt.check_password_hash(newUser.password, form.password.data):
            login_user(newUser, remember=form.rememberMe.data)
            nextPage = request.args.get('next')
            return redirect(nextPage) if nextPage else redirect(url_for('home'))
        else:
            flash(f'Login unsuccesful: Please check email and password.', 'danger')
    return render_template('login.html', title='Login', form=form)
'''
    Logout Route:
        -Logs out the currect user
        -Redirects to homepage
'''
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))
'''
    Resume Route:
        -Only availible if logged in via @login_required decorator
        -Returns resume template if user is logged in
'''
@app.route('/resume')
@login_required
def resume():
    return render_template('resume.html', title='Resume')
