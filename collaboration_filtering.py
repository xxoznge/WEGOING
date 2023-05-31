import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import operator

## 자기가 좋았던 여행지 입력 **
## 나랑 유사한 사용차 찾기
## 리스트 비교 후 없는 내용 출력

places = pd.read_csv('places.csv', encoding='cp949')
# user = pd.DataFrame()

user = pd.read_csv('user.csv', encoding='cp949')
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

## 비슷한 성향의 유저 찾기 - 코사인 유사도
def similar(user_matrix, place_matrix, k=5):
    # matrix의 index = user_id -> 현재 1명 유저에 대한 평가 정보 찾기
    user = user_matrix
    
    # matrix index 값이 user_id와 다른가?
    # 일치하지 않는 값들은 other_users
    other_users = place_matrix
    
    # 대상 user, 다른 유저와의 cosine 유사도 계산 
    # list 변환
    similarities = cosine_similarity(user,other_users)[0].tolist()
    print("similarities\n",similarities)
    # # 다른 사용자의 인덱스 목록 생성
    # other_users_list = other_users.index.tolist()
    
    # # 인덱스/유사도로 이뤄진 딕셔너리 생성
    # # dict(zip()) -> {'other_users_list1': similarities, 'other_users_list2': similarities}
    # user_similarity = dict(zip(other_users_list, similarities))
    
    # # 딕셔너리 정렬
    # # key=operator.itemgetter(1) -> 오름차순 정렬 -> reverse -> 내림차순
    # user_similarity_sorted = sorted(user_similarity.items(), key=operator.itemgetter(1))
    # user_similarity_sorted.reverse()
    
    # # 가장 높은 유사도 k개 정렬하기
    # top_users_similarities = user_similarity_sorted[:k]
    # users = [i[0] for i in top_users_similarities]
    
    # return users

print(similar(user, places, 5))