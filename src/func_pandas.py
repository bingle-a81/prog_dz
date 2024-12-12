import pandas as pd

def data_ecxel(filename):
    df = pd.read_excel(filename, sheet_name="Дневное задание",header=0,index_col=None, usecols="A,B,F,K") 
    ls=('Accutex Al-400SA','ARTA 152 NANO','Laser JPT100','Weld-CNC400','Аутсорсинг','Кооперация','Robodrill','Sunmill')
    df1=df[(df['Кол-во (факт)']==0) & (df['Программа']=='Нет') & (~df['Станок'].isin(ls) )]['Деталь']
    return df1
