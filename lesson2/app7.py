from flask import Flask, request, render_template


import logging
app = Flask(__name__)
logger = logging.getLogger(__name__)
@app.route('/')
def index():
    return '<h1>Hello world!</h1>'

@app.errorhandler(404)
def page_not_found(e):
    logger.warning(e)
    context = {
    'title': 'Страница не найдена',
    'url': request.base_url,
    }
    return render_template('404.html', **context), 404

if __name__ == '__main__':
    app.run(debug=True)