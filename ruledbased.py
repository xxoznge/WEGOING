import numpy as np
import pandas as pd
import csv

#데이터 전처리
df = pd.read_csv('qna.csv', encoding='cp949')
df = df.fillna('0')
df['results'] = df['result1'] + ', ' + df['result2'] + ', ' + df['result3']
df = df.drop(['result1', 'result2', 'result3'], axis=1)

#답변을 abcd로 바꾸기
a=[0]*(len(df))
b=[0]*(len(df))
c=[0]*(len(df))
d=[0]*(len(df))
for i in range(0, len(df),4):
    a[i]=df['answer'][i]
    b[i]=df['answer'][i+1]
    c[i]=df['answer'][i+2]
    d[i]=df['answer'][i+3]

aa = [x for x in a if x != 0]
bb = [x for x in b if x != 0]
cc = [x for x in c if x != 0]
dd = [x for x in d if x != 0]

df['answer'].replace(aa,'a',inplace=True)
df['answer'].replace(bb,'b',inplace=True)
df['answer'].replace(cc,'c',inplace=True)
df['answer'].replace(dd,'d',inplace=True)

# print(df)
# df.to_csv('qqnnaa.csv', encoding='cp949')

#사용자가 선택한 내용을 저장한 csv
ch = pd.read_csv('choose.csv',encoding='cp949')
#print(ch)
# 필요한 리스트 생성
result_list = ['ㄱ']*13

def question(q_num): # 알고리즘
    num = q_num*4 # 행 인덱스
    ques = df[num:num+4] # 관련 질문 행 4개

    if ch['choose'][q_num] == df['answer'][num]:
        result_list[q_num] = df['results'][num]
    elif ch['choose'][q_num] == df['answer'][num+1]:
        result_list[q_num] = df['results'][num]
    elif ch['choose'][q_num] == df['answer'][num+2]:
        result_list[q_num] = df['results'][num]
    elif ch['choose'][q_num] == df['answer'][num+3]:
        result_list[q_num] = df['results'][num]
    
for i in range(0,13):
    question(i)

result_L = [i.replace('0', '').strip(', ') for i in result_list]

print(result_L)