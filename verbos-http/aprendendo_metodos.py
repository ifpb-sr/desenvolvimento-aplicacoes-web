from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

@app.route('/user/<nome>')
def user(nome):
    return '<h1>Hello, {}!</h1>'.format(nome)


if __name__ == '__main__':
    app.run()
