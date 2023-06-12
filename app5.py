from flask import Flask, request, jsonify
import pandas as pd
import sqlite3

app5 = Flask(__name__)

@app5.route('/database_user_input', methods=['POST'])
def database_user_input():
    # 사용자로부터 입력 받기
    data = request.json
    # SQLite 데이터베이스 연결
    conn = sqlite3.connect('place.db3')
    place = pd.DataFrame(columns=['user_id', 'type', 'country', 'city'])
    # 입력값 확인
    if not data:
        return jsonify({'error': 'No data provided'}), 400
    
    # 데이터프레임 생성
    for item in data:
        if isinstance(item, dict):
            name = item.get('name')
            str_num = item.get('num')
            num = int(str_num)
            types = item.get('types')

            for i in range(num):
                country = item.get('country')
                city = item.get('city')

                place = pd.concat([place, pd.DataFrame({'user_id': [name], 'type': [types], 'country': [country], 'city': [city]})], ignore_index=True)
            else:
                # 예외 처리: 문자열인 경우 처리하지 않고 다음 반복으로 넘어감
                continue

    # 생성된 데이터프레임 확인
    print(place)

    # 데이터프레임을 CSV 파일로 저장
    place.to_csv('places.csv', encoding='cp949', index=False)

    # 데이터프레임을 데이터베이스에 추가
    place.to_sql('place_table', conn, if_exists='append', index=False)
    place.to_csv('places.csv',encoding='cp949',index=False)

    # 연결 종료
    conn.close()

    return jsonify({'message': 'User input submitted successfully'})

if __name__ == '__main__':
    app5.run()
