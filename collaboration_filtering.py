import pandas as pd

from like_input import * 

## 자기가 좋았던 여행지 입력 **
## 나랑 유사한 사용차 찾기
## 리스트 비교 후 없는 내용 출력

like = pd.read_csv('ilike.csv', encoding='cp949')
places = pd.read_csv('places.csv', encoding='cp949')

str_num = input("몇 개의 여행지 추천을 하나요?? ")
num = int(str_num)
like_input(num)

same_type = pd.DataFrame(columns=['user_id', 'country', 'city'])
for i in range(len(places)):
   if places['type'][i] == like['type'][0]:
       user = places['user_id'][i]
       country = places['liked_country'][i]
       city = places['liked_city'][i]
       same_type = pd.concat([same_type, pd.DataFrame({'user_id': [user], 'country': [country], 'city': [city]})], ignore_index=True)

print(same_type)
## 일단은 나라만 비교... 도시도 추천 나와야하나?!?!?!?!
sa_li = same_type[~same_type['country'].isin(like['liked_country'])]
print(sa_li)