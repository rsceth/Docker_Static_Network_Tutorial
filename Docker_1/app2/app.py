from flask import Flask
import requests
app = Flask(__name__)

@app.route('/', methods=['GET'])
def get():
    return 'Docker-Compose working!'

@app.route('/check_inter_connection', methods=['GET'])
def check_inter_connection():
    response = requests.get("http://172.4.0.2:5011/flag")
    return response.text

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5012, debug=True)