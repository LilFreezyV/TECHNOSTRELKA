from flask import Flask, render_template, request, make_response
from register_form import RegisterForm
from login_form import LoginForm
import core
import requests
import os

app = Flask('TempName', static_url_path='', static_folder='static')
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


# @app.route('/test')
# def test():
#     env = os.environ.get("ENVIRONMENT")
#     return [env]

# @app.before_request
# def check_login_middleware():
#     # аунтетификация
#     uid = request.cookies.get('uid', None)
#     if uid == None and request.path != '/login' and  not request.path.startswith('/static/'):
#         return app.redirect('/login')


@app.route('/')
def index():
    return app.redirect('/recs')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        is_remember = form.remember_me.data
        uid, success = core.login(username, password)
        if success:
            response = make_response(app.redirect('/recs'))
            response.set_cookie('uid', f'{uid}', max_age=60*60)
            return response
        return render_template('login.html', title='Авторизация', gnev_msg='Неверный логин или пароль', form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/recs')
def recs():
    return render_template(
        'index.html',
        title='Главная',
        ctx=core.get_recs()
    )

@app.route('/find', methods=['POST'])
def find():
    query = request.form['query']
    return render_template(
        'index.html',
        title='Главная',
        ctx=core.get_ctx_for_query(query)
    )

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')