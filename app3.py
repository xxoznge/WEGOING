from flask import Flask, request, jsonify, json
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import sqlite3
import requests
################################################################collaboration_filtering################################################################
app3 = Flask(__name__)

@app3.route('/submit_user_input', methods=['POST'])
def submit_user_input():
    ## 사용자로부터 입력 받기
    data = request.json
    user = pd.DataFrame()
    ## 입력값 확인
    if not data:
        return jsonify({'error': 'No data provided'}), 400
    with open("result.txt", "r") as file:
        type_result = file.read()
    for item in data:
        if isinstance(item, dict):
            name = item.get('name')
            str_num = item.get('num')
            num = int(str_num)
            types = type_result

            for i in range(num):
                country = item.get('country')
                city = item.get('city')

                user = pd.concat([user, pd.DataFrame({'user_id': [name], 'type': [types], 'country': [country], 'city': [city]})], ignore_index=True)
            else:
                ## 예외 처리: 문자열인 경우 처리하지 않고 다음 반복으로 넘어감
                continue

    ## 생성된 데이터프레임 확인
    print(user)

    ## 데이터프레임을 CSV 파일로 저장
    user.to_csv('user_input.csv', encoding='cp949', index=False)
    places = pd.read_csv('places.csv', encoding='cp949')
    pla = sqlite3.connect('place.db3')
    user.to_sql('place_table', pla, if_exists='append', index=False)

    ## B에 A 행 추가
    place = pd.concat([places, user], ignore_index=True)
    place.to_csv('pal.csv',encoding='cp949',index=False)
    return jsonify({'message': 'User input submitted successfully'})

def preprocess_data():
    place = pd.read_csv('pal.csv', encoding='cp949')
    user = pd.read_csv('user_input.csv', encoding='cp949')

    # 중복 행 개수 계산하여 개수 열 채우기 - placea
    duplicates = place.duplicated(subset=[ 'city'])
    grouped_counts = place.groupby(['city']).size().reset_index(name='count')
    place = pd.merge(place, grouped_counts, on=['city'], how='left')
    place['count'] = place['count'].fillna(0).astype(int)

    # 중복 행 개수 계산하여 개수 열 채우기 - user
    user['count'] = 0
    for i in range (0,len(user)):
        user.loc[i, 'count'] = i+1
    
    place.to_csv('plapla.csv',encoding='cp949',index=False)
    place = pd.read_csv('plapla.csv',encoding='cp949')
    return place, user

@app3.route('/recommend', methods=['POST'])
def recommend():
    data = request.json
    k = data.get('k')
    place, user = preprocess_data()

    # 유사도 계산
    # 데이터프레임 샘플링
    first_df_rows = len(place)
    random_number = np.random.randint(0, 10)
    user_sampled = user.sample(n=first_df_rows, replace=True, random_state=random_number)

    # 유사도 계산
    use = user_sampled['count'].values.reshape(1, -1)
    pl = place['count'].values.reshape(1, -1)

    item_similarities = cosine_similarity(use, pl)
    item_similarities = item_similarities.flatten()

    # 유사도가 높은 아이템 추출
    top_items = place.iloc[item_similarities.argsort()[::-1]][:k+1]

    # 추천 결과 반환
    recommendations = top_items[['country', 'city']].to_dict(orient='records')
    item_similarities = item_similarities.tolist()  # ndarray를 리스트로 변환

    return jsonify({"recommendations": recommendations, "item_similarities": item_similarities})

if __name__ == '__main__':
    app3.run()