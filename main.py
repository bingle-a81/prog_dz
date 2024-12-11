import pandas as pd
import numpy as np
import os

df = pd.read_excel("DZ_09.12.2024.xls", sheet_name="Дневное задание",header=0,index_col=None, usecols="A,B,F,K") 

def naz(a:str):
    print(a)

ls=('Accutex Al-400SA','ARTA 152 NANO','Laser JPT100','Weld-CNC400','Аутсорсинг','Кооперация','Robodrill','Sunmill')

df1=df[(df['Кол-во (факт)']==0) & (df['Программа']=='Нет') & (~df['Станок'].isin(ls) )]['Деталь']
ls1=list(df1.values)
# print(ls1)

path_='..\\mk\\'


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

# Пример использования функции
root_directory ='mk\\'
first_level_dirs = get_first_level_directories(root_directory)
# print(first_level_dirs)

for i in ls1:
    if i in first_level_dirs:
        print(i)
    else:
        print('нет')
        

if __name__ == '__main__':
    pass
