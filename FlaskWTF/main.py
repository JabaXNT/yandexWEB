from flask import Flask, url_for, request, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

@app.route('/')
@app.route('/distribution')
def desc():
    member_list = ['Ридли скотт', 'Джеймс Кэмерон', 'Шон Бин']
    return render_template('biba.html', title='По каютам!', mem=member_list)

@app.route('/list_prof/<num>')
def prof(num):
    return render_template('prof.html', title='/list_prof/<num>', num=num, num2=num)

@app.route('/training/<proff>')
def training(proff):
    return render_template('buba.html', title='/training', prof=proff)

@app.route('/index/<title>')
def index(title):
    t = title
    return render_template('base.html', title=t)

@app.route('/table/<sex>/<age>')
def cabinet(sex, age):
    s = sex
    a = int(age)
    return render_template('boba.html', title='цвет каюты', sex=s, age=a)

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
