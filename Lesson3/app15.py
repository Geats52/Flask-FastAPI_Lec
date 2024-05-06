from flask import Flask
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config['SECRET_KEY'] = b'2hg3fcty2ujbh4tfyguij5hg6y7h8j7kljvg'
csrf = CSRFProtect(app)

"""
>>> import secrets
>>> secrets.token_hex()
"""

@app.route('/')
def index():
    return 'HI!'

@app.route('/form', methods=['GET', 'POST'])
@csrf.exempt
def my_form():
    return 'No CSRF protection!'


if __name__ == '__main__':
    app.run(debug=True)
