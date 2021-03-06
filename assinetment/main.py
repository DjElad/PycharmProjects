import json
import pytest
from os import listdir, remove
from os.path import isfile, join, exists
from flask import Flask, Response, redirect, url_for, request, jsonify, render_template
from hello import Todo

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False


def get_todolist():
    path = r"C:\Users\Amir\PycharmProjects\assinetment"
    only_files = [f for f in listdir(path) if isfile(join(path, f))]
    output = []
    for f in only_files:
        if f.endswith(".json"):
            with open(fr"{path}\{f}") as j:
                content = json.load(j)
                output.append(content)
    return output


@app.route('/todos', methods=['POST'])
def create_file():
    user_input = request.json
    chore = Todo(user_input["desc"], user_input["severity"])
    with open(fr"C:\Users\Amir\PycharmProjects\assinetment\{chore.get_uuid()}.json", "w") as f:
        json.dump(chore.to_json(), f)
    return jsonify(chore.to_json()), 201


@app.route('/todos', methods=['GET'])
def all_todos():
    output = get_todolist()
    return jsonify(Todos=output), 201


@app.route('/todos/<task_id>', methods=['GET', 'DELETE', 'PUT'])
def get_task_by_id(task_id):
    output = get_todolist()
    if exists(f"{task_id}.json"):
        if request.method == 'GET':
            with open(fr"C:\Users\Amir\PycharmProjects\assinetment\{task_id}.json", "r") as f:
                uid = json.load(f)
                print(uid)
            return jsonify(uid), 200
    
        elif request.method == 'DELETE':
            remove(f"{task_id}.json")
            print(f"file {task_id}.json was deleted")
            return jsonify({"done": f"file {task_id}.json was deleted"}), 204

        else:
            user_input = request.json
            chore = Todo(user_input["desc"], user_input["severity"])
            if user_input["isDone"]:
                chore.done()
            with open(fr"C:\Users\Amir\PycharmProjects\assinetment\{task_id}.json", "w") as f:
                json.dump(chore.to_json(), f)
            print(f"file {task_id}.json was updated")
            return jsonify({"done": f"file {task_id}.json was updated"}), 204
    
    return jsonify({"error": f"item {task_id} not found"}), 404


if __name__ == '__main__':
    app.run(debug=True, port=8000)
