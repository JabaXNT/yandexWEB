from data import db_session
from data.users import User
from data.jobs import Jobs
from forms.user import RegisterForm
from flask import Flask, render_template, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route("/")
def index():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).filter(Jobs.is_private != True)
    return render_template("index.html", jobs=jobs)


def main():
    db_session.global_init("db/Space.db")
#   app.run()


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            name=form.name.data,
            email=form.email.data,
            about=form.about.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


if __name__ == '__main__':
    main()

user = User()
session = db_session.create_session()
user.surname = "KEkw"
user.name = "Pepega"
user.age = 10010
user.position = "main"
user.speciality = "pog"
user.address = "module_12345"
user.email = "rofl@mars.org"
user.hashed_password = "main_pog"
session.add(user)
session.commit()