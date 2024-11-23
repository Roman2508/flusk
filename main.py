from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/catalog')
def catalog():
    return render_template('catalog.html')


@app.route('/catalog/<id>')
def advertisement(id):
    return render_template('advertisement.html')


@app.route('/create-ad')
def create_ad():
    return render_template('create-ad.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')


if __name__ == '__main__':
    app.run()
