from flask import Flask, request, jsonify, json
import pandas as pd
import ast as ast
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

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


