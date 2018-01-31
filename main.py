"""
Sample python Code to ilustrate a course.
"""
import uuid
from flask import Flask, jsonify, request, session
from helpers import init_session

app = Flask(__name__)

@app.route("/api/todo")
@init_session
def get_list():
    """ Get the current state of the todo memory list """
    return jsonify(session["todo"])

@app.route("/api/todo", methods=['POST'])
@init_session
def save():
    """ Save a new element in the session["todo"] """
    data = request.form
    if "texte" in data:
        session["todo"][str(uuid.uuid4())] = {"texte": data["texte"], "termine": False}
        session.modified = True
        return jsonify({"success": True})
    else:
        return jsonify({"success": False})


@app.route("/api/todo/done/<current_id>", methods=["POST"])
@init_session
def done(current_id):
    """ Mark a todo as done """
    # Id in todo ?
    if current_id in session["todo"]:
        current = session["todo"][current_id]
        current["termine"] = True # Mark As done
        session["todo"][current_id] = current # and Save
        session.modified = True
        return jsonify({"success": True})
    else:
        return jsonify({"success": False})

@app.route("/api/todo/delete/<current_id>", methods=['DELETE'])
@init_session
def delete(current_id):
    """ Remove element from the session["todo"] """
    # current_id exist and mark as done ?
    if current_id in session["todo"] and session["todo"][current_id]["termine"]:
        del session["todo"][current_id] # Remove the data
        session.modified = True
        return jsonify({"success": True})
    else:
        return jsonify({"success": False})

if __name__ == '__main__':
    app.secret_key = 'YOLO_EXAMPLE_CHANGEME'
    app.run()