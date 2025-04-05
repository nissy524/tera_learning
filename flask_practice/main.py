from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/info')
def info():
    data = {
        "name": "terashita",
        "age": 25
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run() 
