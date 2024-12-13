import logging
import os
import shutil

from src import func_folder, func_pandas, make_yaml


a_log=logging.getLogger(__name__)
a_log.warning('test')
      

if __name__ == '__main__':
    df1=func_pandas.data_ecxel("DZ_09.12.2024.xls")    
    root_directory ='УП\\'
    root_directory1='UP\\'
    first_level_dirs = func_folder.get_first_level_directories(root_directory)
    for i in first_level_dirs:
        second_level_dirs=func_folder.get_first_level_directories(root_directory+i+'\\')
        for j in second_level_dirs:
            if j in df1['Деталь'].values:
                therd_level_dirs=func_folder.get_first_level_directories(root_directory+i+'\\'+j+'\\')
                for k in therd_level_dirs:
                    if k in df1['Станок'].values:         
                        shutil.copytree(root_directory+i+'\\'+j+'\\'+k+'\\', root_directory1+i+'\\'+j+'\\'+k+'\\')
                        make_yaml.write_to_yaml_file(j,root_directory1+i+'\\'+j+'\\'+k+'\\')

        

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


