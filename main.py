from flask import Flask
app = Flask(__name__)

@app.route("/api/todo")
def list():
    return ""

@app.route("/api/todo", methods=['POST'])
def save():
    return ""

@app.route("/api/todo/done/<id>")
def done(id):
    return ""

@app.route("/api/todo/delete/<id>", methods=['DELETE'])
def delete(id):
    return ""

if __name__ == '__main__':
    app.run()

