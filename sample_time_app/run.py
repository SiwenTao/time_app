from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, world!'

@app.route('/time')
def current_time():
    time_now = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')
    return 'Current time: {0}'.format(time_now)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
