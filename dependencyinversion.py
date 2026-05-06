# You're developing a to-do app. Initially, you save tasks locally on the phone. Now, you want to add support for saving in the cloud. Can you design it so that you don't have to modify the original code to add the cloud support?
# Python code possible?
# Yes, we can design the to-do app using the Dependency Inversion Principle, which allows us to add new functionality (like cloud support) without modifying the existing code. Below is an example of how to implement this in Python.
# Define an interface for the task storage
class TaskStorage:
    def save_task(self, task):
        pass
    def load_tasks(self):
        pass
# Implement local storage
class LocalTaskStorage(TaskStorage):
    def __init__(self):
        self.tasks = []
    def save_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' saved locally.")
    def load_tasks(self):
        return self.tasks
# Implement cloud storage
class CloudTaskStorage(TaskStorage):
    def __init__(self):
        self.tasks = []
    def save_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' saved in the cloud.")
    def load_tasks(self):
        return self.tasks   
# Task manager that depends on the TaskStorage interface
class TaskManager:
    def __init__(self, storage: TaskStorage):
        self.storage = storage
    def add_task(self, task):
        self.storage.save_task(task)
    def get_tasks(self):
        return self.storage.load_tasks()
# Example usage:
if __name__ == "__main__":
    # Using local storage
    local_storage = LocalTaskStorage()
    task_manager_local = TaskManager(local_storage)
    task_manager_local.add_task("Buy groceries")
    print("Local tasks:", task_manager_local.get_tasks())
    
    # Using cloud storage
    cloud_storage = CloudTaskStorage()
    task_manager_cloud = TaskManager(cloud_storage)
    task_manager_cloud.add_task("Finish project")
    print("Cloud tasks:", task_manager_cloud.get_tasks())
# In this design:   
# - We have defined a `TaskStorage` interface that both `LocalTaskStorage` and `CloudTaskStorage` implement.
# - The `TaskManager` class depends on the `TaskStorage` interface, allowing us to easily switch between local and cloud storage without modifying the `TaskManager` code.
# - This adheres to the Dependency Inversion Principle, as high-level modules (like `   TaskManager`) do not depend on low-level modules (like `LocalTaskStorage` or `CloudTaskStorage`), but both depend on the abstraction (`TaskStorage`).   

