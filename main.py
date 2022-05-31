from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/hello', methods=['GET'])
def helloworld():
	if(request.method == 'GET'):
		data = {"msg": "Hello World"}
		return jsonify(data)

@app.route('/about', methods=['GET'])
def about():
	if(request.method == 'GET'):
		info = {"msg": "first try", "name": "jenu"}
		return jsonify(info)

@app.route('/input', methods=['POST'])
def input():
	body = request.json
	return body

@app.route('/add', methods=['GET', 'POST'])
def addition():
    numbers = request.json
    sum = 0
    for number in numbers['num']:
        sum = sum + number
    return str(sum)

if __name__ == '__main__':
	app.run(debug=True)