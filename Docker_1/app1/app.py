from flask import Flask
import requests
app = Flask(__name__)

@app.route('/', methods=['GET'])
def get():
    return 'Docker-Compose working!'

@app.route('/flag', methods=['GET'])
def flag():
    return "Hello, It's from Docker 1, Container 1!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5011, debug=True)