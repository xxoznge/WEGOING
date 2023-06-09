from flask import Flask, request, jsonify, json
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import operator
################################collaboration_filtering################################
app3 = Flask(__name__)

@app3.route('/submit_user_input', methods=['POST'])
def submit_user_input():
    # 사용자로부터 입력 받기
    data = request.json

    # 입력값 확인
    if not data:
        return jsonify({'error': 'No data provided'}), 400

    # 데이터프레임 생성
    user = pd.DataFrame(columns=['user_id', 'type', 'country', 'city'])
    for item in data:
        if isinstance(item, dict):
            name = item.get('name')
            str_num = item.get('num')
            num = int(str_num)
            types = item.get('types')

            for i in range(num):
                country = item.get('country')
                city = item.get('city')

                user = pd.concat([user, pd.DataFrame({'user_id': [name], 'type': [types], 'country': [country], 'city': [city]})], ignore_index=True)
        else:
            # 예외 처리: 문자열인 경우 처리하지 않고 다음 반복으로 넘어감
            continue

    # 생성된 데이터프레임 확인
    print(user)

    # 데이터프레임을 CSV 파일로 저장
    user.to_csv('user_input.csv', encoding='cp949', index=False)

    return jsonify({'message': 'User input submitted successfully'})

def preprocess_data():
    places = pd.read_csv('places.csv', encoding='cp949')
    user = pd.read_csv('user_input.csv', encoding='cp949')

    # 중복 행 개수 계산
    column = ['country', 'city']
    duplicates = places.duplicated(subset=column)
    counts = places[duplicates].groupby(['country', 'city']).size() + 1

    # 중복 행 삭제
    places.drop_duplicates(subset=column, keep='first', inplace=True)
    places.rename(columns={'Unnamed: 4': 'counts'}, inplace=True)

    # 카테고리를 숫자로 변환
    categories = ['모험가형', '문화 체험형', '휴양형', '음식 여행형', '자유 여행형', '문화 예술형']
    places['EncodedCategory'] = pd.factorize(places['type'])[0] + 1

    # 나라를 숫자로 변환
    places['c_to_n'] = pd.factorize(places['country'])[0]
    factorized_values = pd.factorize(places['c_to_n'])[0]
    unique_categories = places['country']
    converted_values = [unique_categories[index] for index in factorized_values]
    places['n_to_c'] = converted_values

    return places, user

# 비슷한 성향의 유저 찾기 함수
def find_similar_users(user_matrix, place_matrix, k):
    user = user_matrix
    other_users = place_matrix

    u_vec = user[['EncodedCategory', 'c_to_n']].values
    o_vec = other_users[['EncodedCategory', 'c_to_n']].values

    similarities = cosine_similarity(u_vec, o_vec)[0].tolist()
    other_users_list = other_users.index.tolist()

    user_similarity = dict(zip(other_users_list, similarities))
    user_similarity_sorted = sorted(user_similarity.items(), key=operator.itemgetter(1), reverse=True)

    top_users_similarities = user_similarity_sorted[:k]
    users = [i[0] for i in top_users_similarities]

    converted_values = place_matrix['n_to_c'].tolist()
    converted_list = [converted_values[index] for index in users]

    return converted_list

@app3.route('/get_similar_users', methods=['POST'])
def get_similar_users():
    data = request.json
    user_id = data.get('user_id')
    k = data.get('k')

    places, user = preprocess_data()
    similar_users = find_similar_users(user, places, k)

    return jsonify({'similar_users': similar_users})

if __name__ == '__main__':
    app3.run()
