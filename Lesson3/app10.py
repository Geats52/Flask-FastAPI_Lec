from flask import Flask, render_template

#from flask_sqlalchemy import query ???????????

from models_05 import db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../../instance/mydatabase.db'
db.init_app(app)



@app.route('/')
def index():
    return 'HI!'

@app.route('/data/')
def data():
    return 'Your data'

@app.route('/users/')
def all_users():
    users = User.query.all()
    context = {'users': users}
    return render_template('users.html', **context)


if __name__ == '__main__':
    app.run(debug=True)