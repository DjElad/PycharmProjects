from flask import Flask
import json
import uuid


# learn to POST, GET and complete no problems m8
class Todo:

    def __init__(self, desc, severity):
        self.uuid = str(uuid.uuid4())
        self.desc = desc
        self.isDone = False
        self.severity = severity

    def get_uuid(self):
        return self.uuid

    def get_desc(self):
        return self.desc

    def get_severity(self):
        return self.severity

    def done(self):
        self.isDone = True
        return self.isDone

    def is_done(self):
        return self.isDone


task1 = Todo("laundry", 3)
task2 = Todo("dishes", 2)
task3 = Todo("walk the dog", 1)
todo_list = [task1, task2, task3]

app = Flask(__name__)

for i in todo_list:
    with open(f"/\{i.get_uuid()}.json", "w") as f:
        json.dump(data, f)


@app.route('/data')
def hello_admin():
    with open(r"/\file.json", "r") as data_read:
        return json.load(data_read)


if __name__ == '__main__':
    app.run(port=8000, debug=True)
