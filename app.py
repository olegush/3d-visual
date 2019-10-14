from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    """ Главная страница с анимацией """
    return render_template('index.html')


@app.route('/about')
def about():
    """ Страница с контактной информацией"""
    return render_template('about.html')


if __name__ == '__main__':
    app.run()
