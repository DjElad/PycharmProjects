import uuid


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

    def to_json(self):
        return {
            "uuid": self.uuid,
            "desc": self.desc,
            "severity": self.severity,
            "isDone": self.isDone
        }


task1 = Todo("laundry", 3)
task2 = Todo("dishes", 2)
task3 = Todo("walk the dog", 1)
todo_list = [task1, task2, task3]


