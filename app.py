from flask import Flask
from flask import render_template
from flask import request
import core

app = Flask('TempName', static_url_path='', static_folder='static')

@app.route('/')
def index():
    return render_template(
        'index.html',
        title='Главная',
        ctx=core.get_content_for_recs()
    )

@app.route('/find', methods=['POST'])
def find():
    query = request.form['query']
    return render_template(
        'index.html',
        title='Главная',
        ctx=core.get_content_for_query(query)
    )

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')