from flask import render_template, url_for, flash, redirect
from portfolio import app
from portfolio.forms import registerForm, loginForm
from portfolio.dbModel import user
from portfolio.getRepos import handleData

@app.route('/')
@app.route('/home')
def home():
    projects = handleData()
    return render_template('home.html', projects=projects, title="Home")


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = registerForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}', 'success')
        return redirect(url_for('home'))

    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = loginForm()
    if form.validate_on_submit():
        if form.email.data == 'jamiedel818@gmail.com' and form.password.data == 'jamie123':
            flash(f'Login succesful: {form.email.data}', 'success')
            return redirect(url_for('home'))
        else:
            flash(f'Login unsuccesful: Please check email and password.', 'danger')
    return render_template('login.html', title='Login', form=form)
