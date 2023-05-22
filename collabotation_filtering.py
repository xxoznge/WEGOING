import random
import pandas as pd
import statistics
import matplotlib.pyplot as plt

from sklearn.metrics.pairwise import cosine_similarity
import operator

## 자기가 좋았던 여행지 입력 **
## 나랑 유사한 사용차 찾기
## 리스트 비교 후 없는 내용 출력

like = pd.read_csv('ilike.csv', encoding='cp949')
places = pd.read_csv('places.csv', encoding='cp949')
# 좋았던 여행지 입력받기
## 여행지 입력받는 개수를 정해놔야할까?
for i in range(4):
    user_id = input("당신의 별명을 알려주세요 ")
    types = input("당신의 여행 성향은 무엇인가요? ")
    country = input("좋았던 나라는 어디인가요? ")
    city = input("어떤 도시를 여행했나요? ")

    like = like.append({'user_id' : user_id, 'type' : types, 'country' : country, 'city' : city})

same_type = pd.DataFrame(columns=['user_id', 'country', 'city'])
for i in range(len(places)):
    if places['type'][i] == like['type'][0]:
        same_type = same_type.append({'user_id' : places['user_id'][i], 'country' : places['liked_country'][i], 'city' : places['liked_city'][i]})
    

