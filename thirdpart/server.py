from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/demo')
def demo():
    return 'no'


app.run(port=8085)
