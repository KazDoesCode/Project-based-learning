import json

def load_tasks(json_file):
    try:
        with open(json_file, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []
    

def save_tasks(json_file,tasks):
    with open(json_file, "w") as f:
        return json.dump(tasks, f, indent=2)    