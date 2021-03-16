from flask import Flask, url_for, request

app = Flask(__name__)

@app.route('/')
def normal():
    return "Миссия Колонизация Марса"
@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"

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
  
@app.route('/promotion')
def prom():
    ads = ['Человечество вырастает из детства.', 'Человечеству мала одна планета.', 'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!', 'Присоединяйся!']
    return '</br>'.join(ads)

@app.route('/promotion_image')
def mars():
  text = 0
  text2 = 0
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
if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')