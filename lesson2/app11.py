from flask import Flask, flash, redirect, render_template, request, url_for

app = Flask(__name__)

'''
>>> import secrets
>>> secrets.token_hex()
'''

app.secret_key =b'5f214cacbd30c2ae4784b520f17912ae0d5d8c16ae98128e3f549546221265e4'

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        # Обработка данных формы
        flash('Форма успешно отправлена!', 'success')
        return redirect(url_for('form'))
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)