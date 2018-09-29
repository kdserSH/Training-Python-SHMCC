
# coding: utf-8

# In[19]:


import os
import re
import pandas as pd
import sqlite3
from datetime import datetime
from sqlalchemy import create_engine, DateTime, Integer, VARCHAR

LOG_DIR = 'alarm\\'
pat_alarm = re.compile('^(\d)\s+([A-Z][a-z]+)\s+(\d{2}-\d{2}-\d{2})\s+(\d{2}:\d{2}:\d{2})\s+(.+)')
pat_info = re.compile('^\s{32,}(.+)')
columns = ['Ne40', 'Id', 'Level', 'Time', 'Info']
map_dict = {'object':VARCHAR, 'int64':Integer, 'datetime64':DateTime}


# In[20]:


def parse_alarms(alarm_txt, file_name):
    '''
    解析单个告警文件，返回告警dataframe
    格式：['NE', 'Index', 'Level', 'Date', 'Info']
    '''
    alarms_list = pd.DataFrame()
    al_index = None
#     print(file_name)
    for l in alarm_txt:
        alarm = pat_alarm.search(l)
        info = pat_info.search(l)
        if alarm:
            if al_index is not None:
                alarms_list = alarms_list.append([[file_name, al_index, al_level, datetime.strptime(al_date + ' ' + al_time, '%y-%m-%d %H:%M:%S'), al_info]], 
                                                 ignore_index=True)
#                 print(datetime(al_date + ' ' + al_time, '%y-%m-%d %H:%M:%S'))
            al_index = alarm.group(1)
            al_level = alarm.group(2)
            al_date = alarm.group(3)
            al_time = alarm.group(4)
            al_info = alarm.group(5)

        if info:
            al_info = al_info + info.group(1) 
    
    if al_index is not None:
        alarms_list = alarms_list.append([[file_name, al_index, al_level, datetime.strptime(al_date + ' ' + al_time, '%y-%m-%d %H:%M:%S'), al_info]], 
                                         ignore_index=True)
#         print(datetime(al_date + ' ' + al_time, '%y-%m-%d %H:%M:%S'))
    return alarms_list


# In[21]:


def ne_alarms(log_dir):
    '''
    读取所有告警文件并调用parse_alarms解析
    合成并返回一个告警dataframe
    '''
    df = pd.DataFrame()
    for file in os.listdir(log_dir):
        with open(log_dir + file) as f:
            file_name = file[:-4]
            ne_alarms = parse_alarms(f.readlines(), file_name)
        df = pd.concat([df, ne_alarms], ignore_index=True)
    
    df.columns = columns
    # 类型转换
    df['Id'] = df['Id'].astype('int64')
    
    return df


# In[22]:


# if __name__ == '__main__':
#
#     df = ne_alarms(LOG_DIR)
#     print(df.dtypes)
#
#     # 入库
#     engine = create_engine(r'sqlite:///database.db', echo=False)
#     df.to_sql(name='NE40-Alarms', con=engine, if_exists='append', dtype=map_dict, index=False)
#
#     #查询
#     df_read = pd.read_sql('select * from `NE40-Alarms`', con=engine)


# In[18]:


# df_read

