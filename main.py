import logging
import os

from src import func_folder, func_pandas, make_yaml



a_log=logging.getLogger(__name__)
a_log.warning('test')

      

def new_func(df1,  root_directory, root_directory1, bdup_directory):
    first_level_dirs = func_folder.get_first_level_directories(root_directory)
    for i in first_level_dirs:
        second_level_dirs=func_folder.get_first_level_directories(root_directory+i+'\\')
        for j in second_level_dirs:
            if j in df1['Деталь'].values:
                therd_level_dirs=func_folder.get_first_level_directories(root_directory+i+'\\'+j+'\\')
                stanok=df1.loc[df1['Деталь']==j]['Станок']                
                # print(stanok.values[0])
                for k in therd_level_dirs:
                    if k == stanok.values[0]: 
                        for x in func_folder.file_search(root_directory+i+'\\'+j+'\\'+k+'\\'):    
                            # nazv=func_folder.find_name_prog(x)               
                            # naz_level_dirs=func_folder.get_first_level_directories(bdup_directory+func_folder.find_name_prog(x)+'\\'+k+'\\')
                            for _ in func_folder.file_search(os.path.join(bdup_directory,func_folder.find_name_prog(x),k)):
                                func_folder.copy_file(root_directory1+i+'\\'+j+'\\'+k+'\\',_)
                        make_yaml.write_to_yaml_file(j,root_directory1+i+'\\'+j+'\\'+k+'\\')

if __name__ == '__main__':

    excel_dir='c:\\Users\\breat\\OneDrive\\Рабочий стол\\DZ\\'    
    # root_directory_main='c:\\Users\\breat\\python_pr\\prog_dz\\'     
    root_UP ='\\\SERVER2016\\Docs\\УП\\УП\\'
    root_kuda='\\\otk\\Users\\Public\\ДЕТАЛИ\\UP\\'
    bdup_directory='\\\SERVER2016\\Docs\\УП\\АРХИВ\\BdUp\\'
    for ex_file in func_folder.file_search(excel_dir):
        df1=func_pandas.data_ecxel(ex_file) 
        new_func(df1, root_UP, root_kuda, bdup_directory)




