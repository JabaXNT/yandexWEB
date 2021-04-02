from flask import Flask, url_for, request, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

@app.route('/')
@app.route('/index/<title>')
def index(title):
    t = title
    return render_template('base.html', title=t)

@app.route('/list_prof/<num>')
def prof(num):
    return render_template('prof.html', title='/list_prof/<num>', num=num, num2=num)

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
