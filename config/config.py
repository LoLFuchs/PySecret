import json
import os

def get_default_mode(json_file_path="config\config.json"):
    if os.path.exists(json_file_path):
        with open(json_file_path, "r") as file:
            data = json.load(file)
        return data.get("default_mode")
    else:
        return None  
    
def update_default_mode(default_mode, json_file_path="config\config.json"):
    if os.path.exists(json_file_path):
        with open(json_file_path, "r") as file:
            data = json.load(file)
        data["default_mode"] = default_mode
    else:
        data = {
            "default_mode": default_mode
        }
    
    with open(json_file_path, "w") as file:
        json.dump(data, file, indent=4)

def get_default_dir(json_file_path="config\config.json"):
    if os.path.exists(json_file_path):
        with open(json_file_path, "r") as file:
            data = json.load(file)
        return data.get("default_dir", None)
    else:
        return None

def update_default_dir(default_dir, json_file_path="config\config.json"):
    if os.path.exists(json_file_path):
        with open(json_file_path, "r") as file:
            data = json.load(file)
        data["default_dir"] = default_dir
    else:
        data = {
            "default_dir": default_dir
        }
    
    with open(json_file_path, "w") as file:
        json.dump(data, file, indent=4)
        
def clear_default_dir(json_file_path="config\config.json"):
    if os.path.exists(json_file_path):
        with open(json_file_path, "r") as file:
            data = json.load(file)
        data["default_dir"] = "null"
    else:
        data = {
            "default_dir": "null"
        }
    with open(json_file_path, "w") as file:
        json.dump(data, file, indent=4)