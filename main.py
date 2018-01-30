from flask import Flask, jsonify

app = Flask(__name__)
todo_memory = []

@app.route("/api/todo")
def getList():
    """ Get the current state of the todo memory list """
    return jsonify(todo_memory)

@app.route("/api/todo", methods=['POST'])
def save():
    """ Save a new element in the todo_memory """
    return ""

@app.route("/api/todo/done/<current_id>")
def done(current_id):
    """ Mark a todo as done """
    # Id in todo ?
    if current_id in todo_memory:
        current = todo_memory[current_id]
        current["termine"] = True # Mark As done
        todo_memory[current_id] = current # and Save
        return jsonify({"success": True})
    else:
        return jsonify({"success": False})

@app.route("/api/todo/delete/<current_id>", methods=['DELETE'])
def delete(current_id):
    """ Remove element from the todo_memory """
    # current_id exist and mark as done ?
    if current_id in todo_memory and todo_memory[current_id]["termine"]:
        del todo_memory[current_id] # Remove the data
        return jsonify({"success": True})
    else:
        return jsonify({"success": False})

if __name__ == '__main__':
    app.run()