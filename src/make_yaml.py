from encodings.utf_8 import decode
import os, yaml
import time
import codecs

def open_yaml_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return yaml.load(f, Loader=yaml.FullLoader)
    
def write_to_yaml_file(name_prog):
    path = "dict_yaml.yaml"
    dict_programms = {}
    dict_programms.setdefault(name_prog, {})
    dict_programms[name_prog] = {
        "adress": name_prog,
        "prog": dict_programms[name_prog].get("prog", []) ,
    }


    with open(path, "a") as f:
        yaml.dump(dict_programms, f)
        

