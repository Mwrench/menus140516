from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/p1')
def p1():
    return render_template('p1.html')


@app.route('/p2')
def p2():
    return render_template('p2.html')


@app.route('/p3')
def p3():
    return render_template('p3.html')


@app.route('/p4')
def p4():
    return render_template('p4.html')


@app.route('/p5')
def p5():
    return render_template('p5.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/registo')
def registo():
    return render_template('registo.html')


if __name__ == '__main__':
    app.run()
