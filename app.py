from flask import Flask
from flask import render_template, redirect
from flask import request
import core
from register_form import RegisterForm
from login_form import LoginForm
from data import db_session
from data.users import User
from db_manager import get_users, check_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
db_session.global_init("db/users.db")
session = db_session.create_session()

USERNAME = ''


@app.route('/')
def index():
    return render_template(
        'base.html',
        title='Главная',
        ctx=core.get_content_for_recs()
    )


@app.route('/test')
def test():
    return render_template('test.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    global USERNAME
    global IS_LOGIN
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        if username not in get_users():
            surname = form.surname.data
            name = form.surname.data
            number = form.number.data
            email = form.email.data
            password = form.password.data
            is_remember = form.remember_me.data
            user = User()
            user.username = username
            user.surname = surname
            user.name = name
            user.number = number
            user.email = email
            user.password = password
            user.is_remember = is_remember
            session.add(user)
            session.commit()
            USERNAME = username
            IS_LOGIN = True
            return render_template('login_main.html', username=USERNAME)
        IS_LOGIN = False
        return redirect('/login_error')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    global USERNAME
    global IS_LOGIN
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        is_remember = form.remember_me.data
        USERNAME = username
        IS_LOGIN = True
        if check_user(username, password):
            return render_template('login_main.html')
        IS_LOGIN = False
        return 'Проверьте правильность введенных данных'
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/find', methods=['POST'])
def find():
    query = request.form['query']
    return render_template(
        'base.html',
        title='Главная',
        ctx=core.get_content_for_query(query)
    )


@app.route('/login_main')
def login_main():
    return render_template('login_main.html')


@app.route('/login_error')
def login_error():
    return render_template('login_error.html')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
