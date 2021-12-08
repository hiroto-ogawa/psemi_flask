from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route("/")
def index():
    list = []
    for i in range(10):
        list.append(i)
    
    dict = {"nickname": "John", "age": "24", "address": "UK"}

    rand = random.randint(0, 100)

    return render_template('flaskQ.html', list=list, dict=dict, rand=rand)

if __name__ == '__main__':
    app.debug = True
    app.run(port=8000)