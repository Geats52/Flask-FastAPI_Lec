from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'HI!'

@app.route('/index/')
def index():
    context = {
    'title': 'Личный блог',
    'name': 'Харитон',
    }
    return render_template('index2.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
