from tasks import add_tasks, delete_tasks, list_tasks, update_task, filter_tasks
import sys

args = sys.argv

command = args[1]

if command == "add":
    title = args[2]
    add_tasks(title)

elif command == "delete":
    task_id = int(args[2])
    delete_tasks(task_id)

elif command == "update":
    task_id = int(args[2])
    status = args[3]
    update_task(task_id,status)    

elif command == "list":
    if len(args) == 3:
        status = args[2]
        filter_tasks(status)
    else: list_tasks()    

else: print("Unknown command")        