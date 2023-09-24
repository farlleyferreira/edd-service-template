class CheckIntegrations(object):
    def __init__(self):
        ...

    def worker_function(self, task_id):
        print(f"Task {task_id} started")
        result = task_id * 2
        print(f"Task {task_id} completed with result: {result}")
