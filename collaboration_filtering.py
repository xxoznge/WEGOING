import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import operator

## 자기가 좋았던 여행지 입력 **
## 나랑 유사한 사용차 찾기
## 리스트 비교 후 없는 내용 출력

places = pd.read_csv('places.csv', encoding='cp949')
# user = pd.DataFrame()

user = pd.read_csv('user.csv', encoding='cp949')

## 사용자가 추천하는 여행지 입력받기
# name = input("당신의 별명을 알려주세요 ")
# str_num = input("몇 개의 여행지 추천을 하나요?? ")
# num = int(str_num)
# types = input("당신의 여행 성향은 무엇인가요? ")

# for i in range(num):
#     country = input("좋았던 나라는 어디인가요? ")
#     city = input("어떤 도시를 여행했나요? ")

#     user = pd.concat([user, pd.DataFrame({'user_id' : [name], 'type': [types], 'country': [country], 'city': [city]})], ignore_index=True)
## 여행지 리스트 전처리

print(places['country'].dtypes)
places['country'].astype('float')

# # pivot table
# rating_matrix = places.pivot_table(index='user_id', columns='type', values='country')
# # 결측치 제거
# rating_matrix = rating_matrix.fillna(0)
# rating_matrix.shape

# ## 비슷한 성향의 유저 찾기 - 코사인 유사도
# def similar(user_id, matrix, k=5):
#     # matrix의 index = user_id -> 현재 1명 유저에 대한 평가 정보 찾기
#     user = matrix[matrix.index == user_id]
    
#     # matrix index 값이 user_id와 다른가?
#     # 일치하지 않는 값들은 other_users
#     other_users = matrix[matrix.index != user_id]
    
#     # 대상 user, 다른 유저와의 cosine 유사도 계산 
#     # list 변환
#     similarities = cosine_similarity(user,other_users)[0].tolist()
    
#     # 다른 사용자의 인덱스 목록 생성
#     other_users_list = other_users.index.tolist()
    
#     # 인덱스/유사도로 이뤄진 딕셔너리 생성
#     # dict(zip()) -> {'other_users_list1': similarities, 'other_users_list2': similarities}
#     user_similarity = dict(zip(other_users_list, similarities))
    
#     # 딕셔너리 정렬
#     # key=operator.itemgetter(1) -> 오름차순 정렬 -> reverse -> 내림차순
#     user_similarity_sorted = sorted(user_similarity.items(), key=operator.itemgetter(1))
#     user_similarity_sorted.reverse()
    
#     # 가장 높은 유사도 k개 정렬하기
#     top_users_similarities = user_similarity_sorted[:k]
#     users = [i[0] for i in top_users_similarities]
    
#     return users

# ## 예측 모델 생성 - 추천
# def recommend(name, matrix, items=4):
#     # 유저와 비슷한 유저 가져오기
#     similar_users = similar()
#     # dataframe 변환 : 정렬/필터링 용이
#     similar_users_df = pd.DataFrame(similar_users, columns=['user_similarity'])

#     # 현재 사용자의 벡터 가져오기 : matrix = rating_matrix(pivot table)
#     user_df = matrix[matrix.index == name]

#     # 현재 사용자의 평가 데이터 정렬
#     user_df_transposed = user_df.transpose()

#     # 컬럼명 변경 48432 -> rating
#     user_df_transposed.columns = ['rating']

#     # 미시청 콘텐츠는 rating 0로 바꾸어 준다. remove any rows without a 0 value. Anime not watched yet
#     user_df_transposed = user_df_transposed[user_df_transposed['rating']==0]

#     # 안가본 나라 목록리스트 만들기
#     differnt = user_df_transposed.index.tolist()

#     # 안가본 나라 필터링
#     similar_users_df_filtered = similar_users_df[similar_users_df.index.isin(differnt)]

#     # 평균값을 기준으로 내림차순 정렬
#     similar_users_df_ordered = similar_users_df_filtered.sort_values(by=['user_similarity'], ascending=False)

#     # 상위 4개 값 가져오기
#     # items = 4
#     top_n_anime = similar_users_df_ordered.head(items)
#     top_n_anime_indices = top_n_anime.index.tolist()

#     # anime dataframe에서 top10값 찾기
#     information = places[places['country'].isin(top_n_anime_indices)]
#     information
    
#     return information #items

# # 추천 콘텐츠 뽑아내기
# recommend_content = recommend(user['user_id'][0], rating_matrix)

# print("-- 콘텐츠 추천 TOP 10 --")

# # 모든 추천
# print(recommend_content)
# print("===================================")