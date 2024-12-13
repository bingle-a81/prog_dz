import logging
import os
import shutil
from src import func_folder, func_pandas, make_yaml
import re


a_log=logging.getLogger(__name__)
a_log.warning('test')
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
      

if __name__ == '__main__':
    df1=func_pandas.data_ecxel("DZ_09.12.2024.xls")      
    root_directory ='УП\\'
    root_directory1='UP\\'
    bdup_directory='\\\SERVER2016\\Docs\\УП\\АРХИВ\\BdUp\\'
    first_level_dirs = func_folder.get_first_level_directories(root_directory)
    for i in first_level_dirs:
        second_level_dirs=func_folder.get_first_level_directories(root_directory+i+'\\')
        for j in second_level_dirs:
            if j in df1['Деталь'].values:
                therd_level_dirs=func_folder.get_first_level_directories(root_directory+i+'\\'+j+'\\')
                for k in therd_level_dirs:
                    if k in df1['Станок'].values: 
                        for x in file_search(root_directory+i+'\\'+j+'\\'+k+'\\'):    
                            # print(bdup_directory+find_name_prog(x)) 
                            nazv=find_name_prog(x)               
                            naz_level_dirs=func_folder.get_first_level_directories(bdup_directory+find_name_prog(x)+'\\'+k+'\\')
                            for _ in file_search(os.path.join(bdup_directory,find_name_prog(x),k)):
                                copy_file(root_directory1+i+'\\'+j+'\\'+k+'\\',_)
                            # copy_file(root_directory1+i+'\\'+j+'\\'+k+'\\',os.path.join(bdup_directory,find_name_prog(x),k,x))


                        # shutil.copytree(root_directory+i+'\\'+j+'\\'+k+'\\', root_directory1+i+'\\'+j+'\\'+k+'\\')
                        # make_yaml.write_to_yaml_file(j,root_directory1+i+'\\'+j+'\\'+k+'\\')

        

                # print(j,':',therd_level_dirs)
                #     a=df1.loc[df1['Деталь']==j].values
                #     b=list(a)

                # print(os.path.join(*b[0]))





    
    # for i in df1.values:
    #     if i in first_level_dirs:
    #         make_yaml.write_to_yaml_file(i)

    # make_yaml.write_to_yaml_file(a)

    # codecs = ["cp1252", "cp437",  "utf-8"]

    # for codec in codecs:
    #     with open("dict_yaml.yaml", "r", encoding=codec) as file:
    #         text = file.read()
    #     print(codec.rjust(12), "|", text)
    # print("\U0001f600")


