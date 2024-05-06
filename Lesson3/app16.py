from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect
from form_3 import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = b'2hg3fcty2ujbhij5hg6y7h8j7kljvg'
csrf = CSRFProtect(app)

@app.route('/')
def index():
    return 'HI!'

@app.route('/data/')
def data():
    return 'Your data!'

@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate():
    # Обработка данных из формы
        pass
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
