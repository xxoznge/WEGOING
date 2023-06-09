from flask import Flask, request, jsonify, json
import pandas as pd
import ast as ast
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from collections import Counter
import operator

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

def process_data2():
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

def process_data3():
   def cate_to_num(DataFrame):
    categories = ['모험가형', '문화 체험형', '휴양형', '음식 여행형', '자유 여행형', '문화 예술형']
    DataFrame['EncodedCategory'] = pd.factorize(DataFrame['type'])[0] + 1
   def num_to_country(DataFrame):
      cate_to_num(DataFrame)
      DataFrame['c_to_n'] = pd.factorize(DataFrame['country'])[0]
      factorized_values = pd.factorize(DataFrame['c_to_n'])[0]
      #unique_categories = pd.factorize(DataFrame['c_to_n'])[1]
      unique_categories = DataFrame['country']
      # 숫자를 문자열로 변환
      converted_values = [unique_categories[index] for index in factorized_values]
      # 결과를 새로운 열로 추가
      DataFrame['n_to_c'] = converted_values

      # print(DataFrame['n_to_c'])
      return DataFrame
   
   user = pd.DataFrame()
   places = pd.read_csv('places.csv', encoding='cp949')
   # 사용자가 추천하는 여행지 입력받기
   name = input("당신의 별명을 알려주세요 ")
   str_num = input("몇 개의 여행지 추천을 하나요?? ")
   num = int(str_num)
   types = input("당신의 여행 성향은 무엇인가요? ")

   for i in range(num):
      country = input("좋았던 나라는 어디인가요? ")
      city = input("어떤 도시를 여행했나요? ")

      user = pd.concat([user, pd.DataFrame({'user_id' : [name], 'type': [types], 'country': [country], 'city': [city]})], ignore_index=True)

   user.to_csv("user_input.csv", encoding='cp949')

   ## 여행지 리스트 전처리
   # 중복 행 개수 계산
   column = ['country', 'city']
   column_values = places[column].values.tolist()
   duplicates = places.duplicated(subset=column)
   counts = places[duplicates].groupby(['country', 'city']).size() + 1

   # 중복 행 삭제
   places.drop_duplicates(subset=column, keep='first', inplace=True)

   places.rename(columns={'Unnamed: 4' : 'counts'}, inplace=True)

   # pivot table
   rating_matrix = places.pivot_table(index=column, columns='type', values='counts')
   # 결측치 제거
   rating_matrix = rating_matrix.fillna(0)
   rating_matrix.shape

   num_to_country(places)
   num_to_country(user)

   ## 데이터 전처리 끝

   ## 비슷한 성향의 유저 찾기 - 코사인 유사도    ---- 나라 찾기로
   def similar(user_matrix, place_matrix, k):
      # matrix의 index = user_id -> 현재 1명 유저에 대한 평가 정보 찾기
      user = user_matrix
      other_users = place_matrix

      u_vec = user[['EncodedCategory','c_to_n']].values
      o_vec = other_users[['EncodedCategory','c_to_n']].values

      # 대상 user, 다른 유저와의 cosine 유사도 계산 
      # list 변환
      similarities = cosine_similarity(u_vec,o_vec)[0].tolist()
      # 다른 사용자의 인덱스 목록 생성
      other_users_list = other_users.index.tolist()
      
      # 인덱스/유사도로 이뤄진 딕셔너리 생성
      user_similarity = dict(zip(other_users_list, similarities))
      
      # 딕셔너리 정렬
      # key=operator.itemgetter(1) -> 오름차순 정렬 -> reverse -> 내림차순
      user_similarity_sorted = sorted(user_similarity.items(), key=operator.itemgetter(1))
      user_similarity_sorted.reverse()
      
      # 가장 높은 유사도 k개 정렬하기
      top_users_similarities = user_similarity_sorted[:k]
      users = [i[0] for i in top_users_similarities]

      converted_values = places['n_to_c'].to_list()
      converted_list = [converted_values[index] for index in users]
      
      return converted_list
   
   # 결과 (데이터프레임)
   output3= similar(user, places, 2)
   print(output3)

    # 데이터프레임 -> 배열
   outputName = output3["여행지"]
   print(outputName.values)
   outputList = outputName.values

if __name__ == '__main__':
    app.run()