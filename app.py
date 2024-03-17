from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return open('index.html').read()

@app.route('/hello', methods=['POST'])
def hello():
    name = request.form['name']
    #return jsonify(message=f'Hello {name}!')
    return f'Hello {name}!'

if __name__ == '__main__':
    app.run(debug=True)

