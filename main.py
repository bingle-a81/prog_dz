import logging


from src import find_fold, func_pandas


a_log=logging.getLogger(__name__)
a_log.warning('test')
      

if __name__ == '__main__':
    df1=func_pandas.data_ecxel("DZ_09.12.2024.xls")
    root_directory ='mk\\'
    first_level_dirs = find_fold.get_first_level_directories(root_directory)
    for i in df1.values:
        if i in first_level_dirs:
            print(i)
        else:
            print('нет')

