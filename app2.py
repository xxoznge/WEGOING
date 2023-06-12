from flask import Flask, jsonify, request
import pandas as pd
from collections import Counter

from category_mapping import *

app2 = Flask(__name__)

@app2.route("/", methods=["GET"])
def index():
    return "Success"

@app2.route("/process_data", methods=["POST"])
def process_data():
    data = request.get_json()

    ## 데이터 전처리
    qna = pd.read_csv('qna.csv', encoding='cp949')
    ch = pd.read_csv('selected_options.csv', encoding='cp949')
    qna = qna.fillna('0')
    qna['results'] = qna['result1'] + ', ' + qna['result2'] + ', ' + qna['result3']
    qna = qna.drop(['result1', 'result2', 'result3'], axis=1)

    ## 필요한 리스트 생성
    result_list = ['0'] * 13
    resultt = ['0'] * 13
    result_in = ['0'] * 13
    ## 답변을 abcd로 바꾸기
    abcd()
    an_to_abcd()
    ch = pd.read_csv('result_in.csv', encoding='cp949')

    def question(q_num):  ## 알고리즘
        num = q_num * 4  ## 행 인덱스
        if ch['result_in'][q_num] == qna['answer'][num]:
            result_list[q_num] = qna['results'][num]
        elif ch['result_in'][q_num] == qna['answer'][num + 1]:
            result_list[q_num] = qna['results'][num]
        elif ch['result_in'][q_num] == qna['answer'][num + 2]:
            result_list[q_num] = qna['results'][num]
        elif ch['result_in'][q_num] == qna['answer'][num + 3]:
            result_list[q_num] = qna['results'][num]

        return result_list

    ## 결과 리스트
    for i in range(0, 13):
        question(i)
        result_L = [i.replace('0', '').strip(', ') for i in result_list]
        ## 결과를 하나하나 분리
    resultt = [elem for sublst in result_L for elem in sublst.split(", ")]

    ## 뭐가 필요하냐면 비율 따져서 결과 도출하는거
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

    result = cate[max_in]
    print(result)

    return jsonify({"result": result})

if __name__ == '__main__':
    app2.run()