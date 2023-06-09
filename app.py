from flask import Flask, request, jsonify, json
import pandas as pd
import ast as ast
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from collections import Counter
################################content_based################################
app = Flask(__name__)

@app.route("/", methods=["POST"])

def process_data():

    # JSON 파일 전달받기
    dataAll = request.json.get("data")
    print(dataAll)

    # JSON 파일에서 여행지 이름만 추출하기
    dataNeed = (dataAll["travelPastName"])
    print(dataNeed)
    
    # 데이터셋
    travel = pd.read_csv('Travel.csv', encoding='UTF-8')

    # 컬럼 추출 (관광 자원, 여행지)
    data =travel[['관광 자원', '여행지']]
    data[['관광 자원','여행지']].head()
    
    # 유사도 계산
    counter_vector = CountVectorizer(ngram_range=(1,3))
    c_vector_관광자원=counter_vector.fit_transform(data['관광 자원'])
    similarity_관광자원 = cosine_similarity(c_vector_관광자원,c_vector_관광자원 ).argsort()[:,::-1]
    
    def recommend_travel_list(df, 여행지, top =2):
       target_travel_index = df[df['여행지']==여행지].index.values
       sim_index = similarity_관광자원[target_travel_index,:top].reshape(-1)
       sim_index = sim_index[sim_index!=target_travel_index]
       result = df.iloc[sim_index]
       return result
    
    # 결과 (데이터프레임)
    output= recommend_travel_list(data, 여행지=dataNeed)
    print(output)

    # 데이터프레임 -> 배열
    outputName = output["여행지"]
    print(outputName.values)
    outputList = outputName.values
    
    # json 파일로 변환하기
    json_output=outputName.to_json(orient='records')
    return jsonify(json_output)

    dataAll = request.json.get("type")
    print(dataAll)

    #선택지만 추출
    dataNeed = (dataAll["typePastName"])
    print(dataNeed)

    df = pd.read_csv('qna.csv', encoding='cp949')
    df = df.fillna('0')
    df['results'] = df['result1'] + ', ' + df['result2'] + ', ' + df['result3']
    df = df.drop(['result1', 'result2', 'result3'], axis=1)

    qna = pd.read_csv('qna.csv', encoding='cp949')
    #답변을 abcd로 바꾸기
    a=[0]*(len(qna))
    b=[0]*(len(qna))
    c=[0]*(len(qna))
    d=[0]*(len(qna))
    #abcd()
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
    
    output2 = cate[max_in]
    json_output2=output2.to_json(orient='records')
    print(json_output2)

    return jsonify(json_output2)