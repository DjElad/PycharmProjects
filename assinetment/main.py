import json
import uuid
from flask import Flask, Response, redirect, url_for, request, jsonify, render_template
from hello import Todo

app = Flask(__name__)


@app.route('/todos', methods=['POST'])
def create_file():
    user_input = request.json
    chore = Todo(user_input["desc"], user_input["severity"])
    with open(fr"C:\Users\Amir\PycharmProjects\assinetment\{chore.get_uuid()}.json", "w") as f:
        json.dump(chore.to_json(), f)
    return jsonify(chore.to_json())


if __name__ == '__main__':
    app.run(debug=True, port=8000)
