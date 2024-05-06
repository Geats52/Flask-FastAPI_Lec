from flask import Flask

app=Flask(__name__)

@app.route('/')
def index():
    return 'Введи путь к файлу в адресной строке'
@app.route('/<path:file>/')
def get_file(file):
    print(file)
    return f'Ваш файл находится в: {file}!'

if __name__ == '__main__':
    app.run(debug=True)
