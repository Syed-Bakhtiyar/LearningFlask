from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/index')
def hello():
    return render_template('index.html',name = "Bakhtiyar")

@app.route('/list')
def helloList():
    list = [1,2,3,4,5,6,7,8,9,10]
    return render_template('index.html',list = list[:])

@app.route('/inherit')
def inherit():
    return render_template('index2.html',name = "Bakhtiyar")


if '__main__' == __name__:
    app.run(debug=True)