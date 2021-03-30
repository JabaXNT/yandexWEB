from flask import Flask, url_for, request, render_template, redirect, send_from_directory
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/img'

@app.route('/')
@app.route('/astronaut_selection', methods=['POST', 'GET'])
def selection():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Пример формы</title>
                          </head>
                          <body>
                            <h1 style="text-align: center">Анкета претендента</h1>
                            <h2 style="text-align: center">на участие в миссии</h2>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="surname" class="form-control" id="surname" aria-describedby="surnameHelp" placeholder="Введите фамилию" name="surname">
                                    <input type="name" class="form-control" id="name" placeholder="Введите имя" name="name">
                                    <div class="form-group">
                                <form class="login_form" method="post">
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                        <label for="classSelect">Какое у вас образование?</label>
                                        <select class="form-control" id="classSelect" name="class">
                                          <option>Начальное</option>
                                          <option>Основное</option>
                                          <option>Среднее</option>
                                          <option>Среднее (полное)</option>
                                          <option>Высшее</option>
                                        </select>
                                     </div>
                                    <label>Какие у Вас есть профессии?</label>
                                    <div>
                                    <input type="checkbox" name="scales">
                                    <label for="scales">пилот</label>
                                    </div>
                                    <div>
                                    <input type="checkbox" name="horns">
                                    <label for="horns">инженер-исследователь</label>
                                    </div>
                                    <div>
                                    <input type="checkbox" name="horns">
                                    <label for="horns">строитель, экзобиолог</label>
                                    </div>
                                    <div>
                                    <input type="checkbox" name="horns">
                                    <label for="horns">инженер по терраформированию</label>
                                    </div>
                                    <div>
                                    <input type="checkbox" name="horns">
                                    <label for="horns">климатолог</label>
                                    </div>
                                    <div>
                                    <input type="checkbox" name="horns">
                                    <label for="horns">специалист по радиационной защите</label>
                                    </div>                                    
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="about">Почему вы хотите принять участие в миссии?</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Записаться</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['email'])
        print(request.form['password'])
        print(request.form['class'])
        print(request.form['file'])
        print(request.form['about'])
        print(request.form['accept'])
        print(request.form['sex'])
        return "Форма отправлена"
        
@app.route('/index')
def index():
    param = {}
    param['username'] = "Ученик Яндекс.Лицея"
    param['title'] = 'Домашняя страница'
    return render_template('index.html', **param)


@app.route('/image_mars')
def mars():
    text = 'Жди нас, Марс!'
    text2 = 'Вот она какая, красная планета.'
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>{text}</h1>
                    <img src="{url_for('static', filename='img/mars_image.jpg')}" 
                    alt="здесь должна была быть картинка, но она на Марсе">
                    <h4>{text2}<h4>
                  </body>
                </html>"""


@app.route('/choice/<planet_name>')
def choice(planet_name):
  if planet_name == "Плутон":
        return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                   <link rel="stylesheet"
                   href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                   integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                   crossorigin="anonymous">
                    <title>Варианты выбора</title>
                  </head>
                  <body>
                    <h1>Мое предложение: {planet_name}!</h1>
                    <h2>Неплохая планета<h2>
                    <div class="alert alert-primary" role="alert">Жаль что беольше не планета</div>
                    <div class="alert alert-success" role="alert">Но все равно неплохая</div>
                    <div class="alert alert-secondary" role="alert">Может даже получиться колонизировать</div>
                    <div class="alert alert-warning" role="alert">бррррррррр</div>
                    <div class="alert alert-dark alert" role="alert">Присоединяйся!</div>
                  </body>
                </html>'''
  if planet_name == "Земля":
        return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                   <link rel="stylesheet"
                   href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                   integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                   crossorigin="anonymous">
                    <title>Варианты выбора</title>
                  </head>
                  <body>
                    <h1>Мое предложение: {planet_name}!</h1>
                    <h2>Неплохая планета<h2>
                    <div class="alert alert-primary" role="alert">Без слов...</div>
                  </body>
                </html>'''
  return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                   <link rel="stylesheet"
                   href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                   integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                   crossorigin="anonymous">
                    <title>Варианты выбора</title>
                  </head>
                  <body>
                    <h1>Мое предложение: {planet_name}!</h1>
                    <h2>Неплохая планета<h2>
                    <div class="alert alert-primary" role="alert">На ней много необхождимых ресурсов</div>
                    <div class="alert alert-success" role="alert">На ней есть вода и атмосфера</div>
                    <div class="alert alert-secondary" role="alert">на ней есть небольшое магнитное поле</div>
                    <div class="alert alert-warning" role="alert">Наконец она просто красива!</div>
                  </body>
                </html>'''


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def pep(nickname, level, rating):
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                   <link rel="stylesheet"
                   href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                   integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                   crossorigin="anonymous">
                    <title>Результаты</title>
                  </head>
                  <body>
                    <h1>Результаты отбора</h1>
                    <h2>Претендента на участие в миссии {nickname}<h2>
                    <div class="alert alert-success" role="alert">Поздравляем! Ваш рейтинг после {level} этапа отбора</div>
                    <div>составляет {rating}</div>
                    <div class="alert alert-primary" role="alert">Желаем удачи!</div>
                  </body>
                </html>'''


@app.route('/promotion_image')
def mars_prom():
    text3 = "Жди нас, Марс!"
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <link rel="stylesheet"
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                    crossorigin="anonymous">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>{text3}</h1>
                    <img src="{url_for('static', filename='img/mars_image.jpg')}" 
                    alt="здесь должна была быть картинка, но она на Марсе">
                    <div class="alert alert-primary" role="alert">Человечество вырастает из детства.</div>
                    <div class="alert alert-success" role="alert">Человечеству мала одна планета.</div>
                    <div class="alert alert-secondary" role="alert">Мы сделаем обитаемыми безжизненные пока планеты.</div>
                    <div class="alert alert-warning" role="alert">И начнем с Марса!</div>
                    <div class="alert alert-dark alert" role="alert">Присоединяйся!</div>
                  </body>
                </html>"""
  

@app.route('/load_photo', methods=['POST', 'GET'])
def loda():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                             <link rel="stylesheet"
                             href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                             integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                             crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                            <h1 style="text-align: center">Загрузка фотографии</h1>
                            <h2 style="text-align: center">Для участия в миссии</h2>                         
                            <form class="login_form" method="post" enctype="multipart/form-data">
                            <label>Приложите фотографию</label>
                               <div class="form-group">
                                    <input type="file" class="form-control-file" id="photo" name="file">
                                </div>
                                <button type="submit" class="btn btn-primary">Отправить</button>
                            </form>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        f = request.files['file']
        filename = (f.filename)
        pep = str(filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                             <link rel="stylesheet"
                             href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                             integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                             crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                            <h1 style="text-align: center">Загрузка фотографии</h1>
                            <h2 style="text-align: center">Для участия в миссии</h2>                         
                            <form class="login_form" method="post" enctype="multipart/form-data">
                            <label>Приложите фотографию</label>
                            <img src="static/img/{pep}" 
                            alt="здесь должна была быть картинка, но она на Марсе">
                               <div class="form-group">
                                    <input type="file" class="form-control-file" id="photo" name="file">
                                </div>
                                <button type="submit" class="btn btn-primary">Отправить</button>
                            </form>
                          </body>
                        </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
