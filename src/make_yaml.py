import yaml

def open_yaml_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return yaml.load(f, Loader=yaml.FullLoader)
    
def write_to_yaml_file(name_prog,addres):
    path = "dict_yaml.yaml"
    dict_programms = {}
    dict_programms.setdefault(name_prog, {})
    dict_programms[name_prog] = {
        "adress": addres,
        # "prog": dict_programms[addres].get("prog", []) ,
    }
    with open(path, "a",encoding="utf-8") as f:
        yaml.dump(dict_programms, f,allow_unicode=True)
        

