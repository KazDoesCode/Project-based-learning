import pytest
import os
import io
import sys
from tasks import add_tasks, delete_tasks,get_status , list_tasks, update_task, filter_tasks
from storage import load_tasks, save_tasks

test_file = "test.json"

def test_add_tasks():
# 1. Setup    
    with open(test_file, "w") as f:
        f.write("[]")

# 2. Act
    add_tasks("test task", json_file=test_file)
    
# 3. Assert
    tasks = load_tasks(test_file)
    assert len(tasks) == 1
    assert tasks[0]["id"] == 1
    assert tasks[0]["title"] == "test task"
    assert tasks[0]["done"] is False
    assert tasks[0]["in_progress"] is True

# 4. Cleanup
    os.remove(test_file)


def test_delete_tasks():   
    with open(test_file, "w") as f:
        f.write("[]")

    for num in range(1,4):
        add_tasks(f"test task {num}", test_file)
    delete_tasks(2, test_file)  

    tasks = load_tasks(test_file)
    assert len(tasks) == 2
    assert tasks[1]["id"] == 2
    assert tasks[1]["title"] == "test task 3"
    assert tasks[0]["done"] is False
    assert tasks[0]["in_progress"] is True

    os.remove(test_file) 

def test_list_tasks():
# 1. Setup    
    with open(test_file, "w") as f:
        f.write("[]")

# 2. Act
    for num in range(1,4):
        add_tasks(f"test task {num}", test_file)

    captured_output = io.StringIO()  # créer un "faux stdout"
    sys.stdout = captured_output    # rediriger stdout    

    list_tasks(json_file=test_file) 

    sys.stdout = sys.__stdout__ # Restaurer stdout
    
# Construire l'attendu
    tasks = load_tasks(test_file)
    expected_output = ""

    for task in tasks:
        expected_output += f'ID: {task["id"]} | Title: {task["title"]} | Status: {get_status(task)}\n'

    assert expected_output == captured_output.getvalue()

    os.remove(test_file)    