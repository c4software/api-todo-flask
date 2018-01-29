from flask import Flask
app = Flask(__name__)

@app.route("/api/list")
@app.route("/api/")
def list():
    return ""

if __name__ == '__main__':
    app.run()

