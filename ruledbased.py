import numpy as np
import pandas as pd
from collections import Counter

from category_mapping import *

#데이터 전처리
df = pd.read_csv('qna.csv', encoding='cp949')
df = df.fillna('0')
df['results'] = df['result1'] + ', ' + df['result2'] + ', ' + df['result3']
df = df.drop(['result1', 'result2', 'result3'], axis=1)

#답변을 abcd로 바꾸기
a=[0]*(len(qna))
b=[0]*(len(qna))
c=[0]*(len(qna))
d=[0]*(len(qna))
abcd()

#사용자가 선택한 내용을 저장한 csv
ch = pd.read_csv('choose.csv',encoding='cp949')

# 필요한 리스트 생성
result_list = ['0']*13
resultt = ['0']*13

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
    
    return result_list

###################################

# 결과 리스트 
for i in range(0,13):
    question(i)
    result_L = [i.replace('0', '').strip(', ') for i in result_list]
    # 결과를 하나하나 분리
resultt = [elem for sublst in result_L for elem in sublst.split(", ")]

#뭐가 필요하냐면 비율 따져서 결과 도출하는거
counted = Counter(resultt)

def count():
    c = Counter(resultt)
    free = c['자유 여행형'] / 15
    rest = c['휴양형'] / 12
    art = c['문화 예술형'] / 12
    exp = c['문화 체험형'] / 14
    food = c['음식 여행형'] / 9
    tam = c['모험가형'] / 10

    cate = ['free', 'rest', 'art', 'exp', 'food', 'tam']
    numbers = [free, rest, art, exp, food, tam]
    max_num = max(numbers)
    max_in = numbers.index(max_num)
    return cate[max_in]

print(count)