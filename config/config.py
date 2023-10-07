import json
import os

def SaveConfig(newData,path="config\config.json"):
    if os.path.exists(path):
        with open(path,"w") as file:
            data = json.load(file)
        
        
    data = newData

    with open(path, 'w') as file:
        json.dump(data, file, indent=4)
