from flask import Flask, render_template, request, make_response, redirect
from register_form import RegisterForm
from login_form import LoginForm
import core
import requests
import os

app = Flask('Technostrelka2025', static_url_path='', static_folder='static')
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def is_login():
    uid = request.cookies.get('uid', None)
    return uid != None


@app.route('/')
def index():
    if not is_login():
        return redirect('/login')
    return redirect('/recs')

@app.route('/exit')
def exit():
    response = make_response(app.redirect('/login'))
    response.set_cookie('uid', '', expires=0)
    return response


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        is_remember = form.remember_me.data
        uid, success = core.login(
            form.username.data,
            form.password.data
        )
        if success:
            response = make_response(app.redirect('/recs'))
            response.set_cookie('uid', f'{uid}', max_age=60 * 60)
            return response
        return render_template('login.html', title='Авторизация', gnev_msg='Неверный логин или пароль', form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        is_remember = form.remember_me.data
        uid, success = core.register(
            form.username.data,
            form.surname.data,
            form.name.data,
            form.number.data,
            form.email.data,
            form.password.data
        )
        if success:
            response = make_response(app.redirect('/recs'))
            response.set_cookie('uid', f'{uid}', max_age=60 * 60)
            return response
        return render_template('register.html', title='Регистрация', gnev_msg='Логин уже занят, попробуйте другой',
                               form=form)
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/recs')
def recs():
    if not is_login():
        return redirect('/login')
    uid = request.cookies.get('uid', None)
    res = core.get_recs(uid)
    if res['status'] == 'error':
        return render_template(
            'sorry.html',
            username=core.get_username(uid)
        )
    return render_template(
        'index.html',
        title='Главная',
        ctx=res['content'],
        username=core.get_username(uid)
    )


@app.route('/find', methods=['POST'])
def find():
    if not is_login():
        return redirect('/login')
    query = request.form['query']
    uid = request.cookies.get('uid', None)
    return render_template(
        'index.html',
        title='Главная',
        ctx=core.get_ctx_for_query(query, uid),
        username=core.get_username(uid)
    )


if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')
