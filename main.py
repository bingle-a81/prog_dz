import logging



from src import func_folder, func_pandas, make_yaml


a_log=logging.getLogger(__name__)
a_log.warning('test')
      

if __name__ == '__main__':
    df1=func_pandas.data_ecxel("DZ_09.12.2024.xls")
    root_directory ='mk\\'
    first_level_dirs = func_folder.get_first_level_directories(root_directory)
    for i in df1.values:
        if i in first_level_dirs:
            make_yaml.write_to_yaml_file(i)

    print('\u0418\u042E\u041C\u041A.715513.017.hat')


