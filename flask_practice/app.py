from flask import Flask, render_template, jsonify
app = Flask(__name__)

@app.route('/index')
def index():
    return render_template('index.html') # templatesフォルダ内のindex.htmlを表示する

@app.route('/info')
def info():
    data = {
        "name": "terashita",
        "age": 25
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run()