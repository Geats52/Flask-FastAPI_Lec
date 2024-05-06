from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'HI!'

@app.route('/if/')
def index():
    context = {
    'title': 'Личный блог',
    'name': 'Харитон',
    'number': 1,
    }
    return render_template('show_if.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
