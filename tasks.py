import json
import os
from storage import load_tasks, save_tasks
  
STATUS_MAP = {
    "done": (True, False),
    "in_progress": (False, True),
    "not_done": (False, False)
}


def add_tasks(title):
    tasks = load_tasks("data.json") 
    
    new_task = {
        "id": len(tasks) + 1,
        "title": title,
        "done": False,
        "in_progress": True
    }
    tasks.append(new_task)
    save_tasks("data.json",tasks)        

def delete_tasks(task_id):
    tasks = load_tasks("data.json")

    tasks = [task for task in tasks if task["id"] != task_id]
    for index, task in enumerate(tasks):
        task["id"] = index + 1

    save_tasks("data.json",tasks)

def get_status(task):
        if task["done"] == True:
            return "Done"
        elif task["in_progress"] == True:
            return "In progress"
        else: return "Pending"         


def display_tasks(task):
    print(f'ID: {task["id"]} | Title: {task["title"]} | Status: {get_status(task)}')
    
def list_tasks():
    tasks = load_tasks("data.json")
    for task in tasks:
        display_tasks(task)

def filter_tasks(status):
    tasks = load_tasks("data.json")
    status = status.lower()
    for task in tasks:
        if status == "done" and task["done"] == True:
            display_tasks(task)
        elif status == "in_progress" and task["in_progress"] == True:
            display_tasks(task)
        elif status == "not_done" and task["in_progress"] == False and task["done"] == False:
            display_tasks(task)       

def update_task(task_id, status):
    tasks = load_tasks("data.json")
    status = status.lower()
    for task in tasks:
        if task["id"] == task_id:
            task["done"], task["in_progress"] = STATUS_MAP[status]                                    
    save_tasks("data.json",tasks)            