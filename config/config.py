import json
import os

def SaveConfig(data,path="config\config.json"):
    if os.path.exists(path):
        pass
    else:
        with open(path, 'w') as file:
            json.dump(data, file, indent=4)
