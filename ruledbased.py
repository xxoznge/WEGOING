import numpy as np
import pandas as pd
from collections import Counter

from category_mapping import *

#데이터 전처리
qna = pd.read_csv('qna.csv', encoding='cp949')
qna = qna.fillna('0')
qna['results'] = qna['result1'] + ', ' + qna['result2'] + ', ' + qna['result3']
qna = qna.drop(['result1', 'result2', 'result3'], axis=1)

#답변을 abcd로 바꾸기
a=[0]*(len(qna))
b=[0]*(len(qna))
c=[0]*(len(qna))
d=[0]*(len(qna))
def abcd():
    for i in range(0, len(qna),4):
        a[i]=qna['answer'][i]
        b[i]=qna['answer'][i+1]
        c[i]=qna['answer'][i+2]
        d[i]=qna['answer'][i+3]

    aa = [x for x in a if x != 0]
    bb = [x for x in b if x != 0]
    cc = [x for x in c if x != 0]
    dd = [x for x in d if x != 0]

    qna['answers'] = qna['answer']    #필요한가...?

    qna['answer'].replace(aa,'a',inplace=True)
    qna['answer'].replace(bb,'b',inplace=True)
    qna['answer'].replace(cc,'c',inplace=True)
    qna['answer'].replace(dd,'d',inplace=True)

    return a, b, c, d
abcd()

#사용자가 선택한 내용을 저장한 csv
ch = pd.read_csv('selected_options.csv',encoding='cp949')

# 필요한 리스트 생성
result_list = ['0']*13
resultt = ['0']*13

def question(q_num): # 알고리즘
    num = q_num*4 # 행 인덱스
    ques = qna[num:num+4] # 관련 질문 행 4개

    if ch['choose'][q_num] == qna['answer'][num]:
        result_list[q_num] = qna['results'][num]
    elif ch['choose'][q_num] == qna['answer'][num+1]:
        result_list[q_num] = qna['results'][num]
    elif ch['choose'][q_num] == qna['answer'][num+2]:
        result_list[q_num] = qna['results'][num]
    elif ch['choose'][q_num] == qna['answer'][num+3]:
        result_list[q_num] = qna['results'][num]
    
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

free = counted['자유 여행형'] / 15
rest = counted['휴양형'] / 12
art = counted['문화 예술형'] / 12
exp = counted['문화 체험형'] / 14
food = counted['음식 여행형'] / 9
tam = counted['모험가형'] / 10

type = pd.read_csv("type.csv", encoding='cp949')
cate = type['type']
numbers = [free, rest, art, exp, food, tam]
max_num = max(numbers)
max_in = numbers.index(max_num)

print(cate[max_in])