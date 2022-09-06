#Import package
from flask import Flask 

app = Flask(__name__)

#Assigned routes and messages for each 
@app.route('/')
def hello():
    return '<h1>Hello, World!</h1>'

@app.route('/home')
def home():
    return '<h1>This is the home page</h1>'

@app.route('/faq')
def faq():
    return '<h1>Here are some frequently asked questions</h1>'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)