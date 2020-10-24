import json
from os import listdir
from os.path import isfile, join
from flask import Flask, Response, redirect, url_for, request, jsonify, render_template
from hello import Todo

app = Flask(__name__)


@app.route('/todos', methods=['POST'])
def create_file():
    user_input = request.json
    chore = Todo(user_input["desc"], user_input["severity"])
    with open(fr"C:\Users\Amir\PycharmProjects\assinetment\{chore.get_uuid()}.json", "w") as f:
        json.dump(chore.to_json(), f)

    return jsonify(chore.to_json()), 201


@app.route('/todos', methods=['GET'])
def all_todos():
    path = r"C:\Users\Amir\PycharmProjects\assinetment"
    only_files = [f for f in listdir(path) if isfile(join(path, f))]
    output = []
    for f in only_files:
        if f.endswith(".json"):
            with open(fr"{path}\{f}") as j:
                content = json.load(j)
                output.append(content)
    return jsonify(Todos=output), 201


if __name__ == '__main__':
    app.run(debug=True, port=8000)
