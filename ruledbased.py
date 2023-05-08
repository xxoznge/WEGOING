import numpy as np
import pandas as pd
import csv

df = pd.read_csv('qna.csv', encoding='cp949')
df = df.fillna('0')
df['results'] = df['result1']+df['result2']+df['result3']
df = df.drop(['result1', 'result2', 'result3'], axis=1)
# print(df)
df.to_csv('qqnnaa.csv', encoding='cp949')
result_list = []
choose = []

# for i in range(0, len(df), 4):
#     sliced_df = df.iloc[i:i+4]
#     print(sliced_df)


def question(q_num):
    num = q_num*4
    ques = df[num:num+4]
    if choose[q_num] == df['answer'][num]:
        result_list[q_num] = df['reslut']
    result = result_list[q_num]
