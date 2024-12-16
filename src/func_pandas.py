import pandas as pd

def zamena(x):
    machine_dict={'Nomura NN32-YB3': ['Nomura NN-32YB3'],
                   'Nomura NN-10E': ['Nomura NN-10E'],
                     'Nomura NN-20J2(1,2,3)': ['Nomura NN-20J2 (1)', 'Nomura NN-20J2 (2)', 'Nomura NN-20J2 (3)'],
                       'Nomura NN-20J3(4,5)': ['Nomura NN-20J3 (4)', 'Nomura NN-20J3 (5)'],
                         'Nomura NN-20J3XB80(6)': ['Nomura NN-20J3 (6)'], 
                         'Tsugami BO126 TF-III': ['Tsugami BO126TF-III'],
                           'Tsugami BO126 TF-V': ['Tsugami BO126TF-5'], 
                           'Tsugami SS267-III': ['Tsugami SS267-III'],
                             'Tsugami M08SY-II': ['Tsugami M08SY-II'], 
                             'Hanhwa XD20H': ['Hanwha XD20H'],
                             'Nexturn SA-26PY': ['Nexturn SA-26PY'],
                             'Nexturn SA-12B': ['Nexturn SA-12B (1)', 'Nexturn SA-12B (2)'],
                               'Miyano BNJ-42SY': ['Miyano BNJ-42SY'],
                                 'Colchester T8MSY': ['Colchester T8MSY'],
                                   'SMEC-NS2100SY': ['SMEC NS2100SY'],
                                     'Citizen Cincom L12(1)': ['Citizen Cincom L12 (1)'],
                                     'Citizen Cincom L12(2)': ['Citizen Cincom L12 (2)'],
                                       'TFC-125': ['TFC-125'], 'IRT': ['IRT'], 
                                       'NomuraNN-16UB5': ['Nomura NN-16UB5']}    
    for k,v in machine_dict.items():
        for a in v:
            if a==x:
                return k

def data_ecxel(filename):
    # sheet_name="Дневное задание",
    df = pd.read_excel(filename, header=0,index_col=None, usecols="A,B,F,K") 
    ls=('Accutex Al-400SA','ARTA 152 NANO','Laser JPT100','Weld-CNC400','Аутсорсинг','Кооперация','Robodrill','Sunmill')
    df1=df[(df['Кол-во (факт)']==0) & (df['Программа']=='Нет') & (~df['Станок'].isin(ls) )][['Деталь','Станок']]
    df1['Станок']=df1['Станок'].apply(zamena)
    return df1
