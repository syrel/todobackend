from models import Task

from gt_examples import (example, Assert)


class TaskExamples:
    @example
    def default_task(self):
        task = Task('Hello')
        Assert.equals(task.get_content(), 'Hello')
        Assert.equals(task.is_completed(), False)
        return task

    @example
    def task_set_content(self):
        task = self.default_task()
        task.set_content('World')
        Assert.equals(task.get_content(), 'World')
        return task

    @example
    def task_be_completed(self):
        task = self.default_task()
        task.be_completed()
        Assert.equals(task.is_completed(), True)
        return task

    @example
    def default_task_as_dictionary(self):
        task = self.default_task()
        dictionary = task.as_dictionary()
        Assert.equals(dictionary, {
            'uuid': task.get_uuid(),
            'content': 'Hello',
            'completed': False
        })
        return dictionary

    def not_example(self):
        return 1
