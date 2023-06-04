import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import operator

from category_mapping import *

## 자기가 좋았던 여행지 입력 **
## 나랑 유사한 사용차 찾기
## 리스트 비교 후 없는 내용 출력

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
#counts = places[duplicates].groupby('country').size() + 1
counts = places[duplicates].groupby(['country', 'city']).size() + 1

# 중복 행 삭제
places.drop_duplicates(subset=column, keep='first', inplace=True)
#places["count"] = counts

places.rename(columns={'Unnamed: 4' : 'counts'}, inplace=True)
# places.to_csv("pl.csv", encoding='cp949')
# # 중복 행 개수 및 리스트 출력
# print("중복 행 개수:")
# print(counts)

# pivot table
rating_matrix = places.pivot_table(index=column, columns='type', values='counts')
# 결측치 제거
rating_matrix = rating_matrix.fillna(0)
rating_matrix.shape

num_to_country(places)
num_to_country(user)
#places.to_csv("pp.csv", encoding='cp949')

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
    # dict(zip()) -> {'other_users_list1': similarities, 'other_users_list2': similarities}
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

print(similar(user, places, 2))