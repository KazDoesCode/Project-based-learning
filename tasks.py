import json
import os
from storage import load_tasks, save_tasks
  
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

def list_tasks():
    tasks = load_tasks("data.json")
    for task in tasks:
        if task["done"] == True:
            status = "Done"
        elif task["in_progress"] == True:
            status = "In progress"
        else: status = "Pending"         
        print(f'ID: {task["id"]} | Title: {task["title"]} | Status: {status}')

def filter_tasks(status):
    tasks = load_tasks("data.json")
    for task in tasks:
        if status.lower() == "done" and task["done"] == True:
            print(f'ID: {task["id"]} | Title: {task["title"]} | Status: Done')
        elif status.lower() == "in_progress" and task["in_progress"] == True:
            print(f'ID: {task["id"]} | Title: {task["title"]} | Status: In progress')
        elif status.lower() == "not_done" and task["in_progress"] == False and task["done"] == False:
            print(f'ID: {task["id"]} | Title: {task["title"]} | Status: Not done')       

            



def update_task(task_id, status):
    tasks = load_tasks("data.json")
    for task in tasks:
        if task["id"] == task_id:
            if status.lower() == "done":
                task["done"] = True
                task["in_progress"] = False
            elif status.lower() == "in_progress":
                task["done"] = False
                task["in_progress"] = True
            elif status.lower() == "not_done":
                task["done"] = False
                task["in_progress"] = False                                     
    save_tasks("data.json",tasks)            