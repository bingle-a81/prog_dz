import os
def get_first_level_directories(root_dir):
    directories = []
    
    # Получаем список содержимого корневой директории
    contents = os.listdir(root_dir)
    
    # Фильтруем только те элементы, которые являются каталогами
    for item in contents:
        full_path = os.path.join(root_dir, item)
        if os.path.isdir(full_path):
            directories.append(item)
            
    return directories  