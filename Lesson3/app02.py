from flask import Flask
from models_02 import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)



@app.route('/')
def index():
    return 'HI!'

if __name__ == '__main__':
    app.run(debug=True)
