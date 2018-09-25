from uuid import uuid4


class Task:
    def __init__(self,content):
        self.uuid = str(uuid4())
        self.completed = False
        self.content = content

    def set_content(self,content):
        self.content = content

    def be_completed(self):
        self.completed = True

    def is_completed(self):
        return self.completed

    def get_uuid(self):
        return self.uuid

    def get_content(self):
        return self.content

    def as_dictionary(self):
        return {
            'uuid': self.uuid,
            'content': self.content,
            'completed': self.completed
        }
