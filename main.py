from flask import Flask, jsonify

app = Flask(__name__)
todo_memory = []

@app.route("/api/todo")
def getList():
    return jsonify(todo_memory)

@app.route("/api/todo", methods=['POST'])
def save():
    return ""

@app.route("/api/todo/done/<id>")
def done(id):
    # Id in todo ?
    if id in todo_memory:
        current = todo_memory[id]
        current["termine"] = True # Mark As done
        todo_memory[id] = current # and Save
        return jsonify({"success": True})
    else:
        return jsonify({"success": False})

@app.route("/api/todo/delete/<id>", methods=['DELETE'])
def delete(id):
    return ""

if __name__ == '__main__':
    app.run()