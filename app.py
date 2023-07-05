from flask import Flask, request,jsonify
import requests
import time

app = Flask(__name__)
start_time = None

@app.route('/strategy', methods=['POST'])
def strategy():
    global start_time
    start_time = time.time()
    requests.get('http://10.251.64.98:4000/api/clear_logs')
    requests.post('http://10.251.64.98:4000/api/strategy', data={"id":"123456"})
    return f'Enviado para execução, configra o log em /stragey_log '

@app.route('/strategy_log', methods=['GET'])
def strategy_log():
    logs = requests.get('http://10.251.64.98:4000/api/logs')
    return f'Logs: {logs.text}'


@app.route('/strategy2', methods=['POST'])
def strategy2():
    global start_time
    start_time = time.time()
    response=requests.post('http://10.251.64.98:4000/api/strategy2', data={"id":"123456"})
    end_time = time.time()
    elapsed_time = end_time - start_time
    return f'Tempo de execução: {elapsed_time} seconds, {response.text}'


@app.route('/strategy3', methods=['POST'])
def strategy3():
    global start_time
    start_time = time.time()
    requests.get('http://10.251.64.98:4000/api/clear_logs')
    requests.post('http://10.251.64.98:4000/api/strategy', data={"id":"123456"})
    return f'Strategy started ...'

@app.route('/event', methods=['POST'])
def event():
    global start_time
    response=request.get_json()
    end_time = time.time()
    elapsed_time = end_time - start_time
    return f'Tempo de execução: {elapsed_time} seconds, {response}'

@app.route('/health', methods=['GET'])
def health():
    return "Api is working"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
