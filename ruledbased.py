import numpy as np
import pandas as pd
import csv

#데이터 전처리
df = pd.read_csv('qna.csv', encoding='cp949')
df = df.fillna('0')
df['results'] = df['result1'] + ', ' + df['result2'] + ', ' + df['result3']
df = df.drop(['result1', 'result2', 'result3'], axis=1)
# print(df)
# df.to_csv('qqnnaa.csv', encoding='cp949')

# 필요한 리스트 생성
result_list = []
choose = [] # 가져와야하는 리스트....

def question(q_num): # 규칙기반알고리즘
    num = q_num*4 # 행 인덱스
    ques = df[num:num+4] # 관련 질문 행 4개

    if choose[q_num] == df['answer'][num]:
        result_list[q_num] = df['resluts']
    elif choose[q_num] == df['answer'][num+1]:
        result_list[q_num] = df['resluts']
    elif choose[q_num] == df['answer'][num+2]:
        result_list[q_num] = df['resluts']
    elif choose[q_num] == df['answer'][num+3]:
        result_list[q_num] = df['resluts']


