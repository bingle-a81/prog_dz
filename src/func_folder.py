import os
import shutil
import re

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

def copy_file(path_folder_kuda,path_folder_otkuda):
    a=path_folder_otkuda.split('\\')[-1]
    if os.path.isdir(path_folder_kuda) == False:
        os.makedirs(path_folder_kuda)
    shutil.copyfile(path_folder_otkuda,os.path.join(path_folder_kuda,a))
def correction_name(string):  # удаляем символы кроме букв,цифр и точки
    reg = re.compile("[^a-zA-Z0-9. -]")
    a = reg.sub("", string)
    return a.strip().rstrip(".")
def chenge_name(st):  # удаляем расширение файла
    if st.rfind(".") > 0:
        return st[0 : st.rfind(".")]
    return st

def file_search(path):  # ищем файл в папке  со станков
    for adress, dirs, files in os.walk(path):
        for file in files:
            if not file.endswith('zip'):
                adress_file_in_check = os.path.join(adress, file)
                yield adress_file_in_check  # возвращаем адрес файла

def find_name_prog(filename):
    # try:
    with open(filename, "r", encoding="windows-1252") as r:  # только чтение файла
        i = 0
        while i < 3:
            st = r.readline()  # чтение текстового файла построчно
            i += 1
            if ("(" in st) and (")" in st):
                f_name = st[(st.index("(") + 1) : (st.index(")"))].strip()
                f_name = correction_name(f_name).strip()
                return f_name
        else:
            return chenge_name(filename.split("\\")[-1])  # если в файле названия нет - берем имя файла
    # except UnicodeDecodeError as u:
    #     print(u)