import pandas as pd

## 자기가 좋았던 여행지 입력 **
## 나랑 유사한 사용차 찾기
## 리스트 비교 후 없는 내용 출력

like = pd.read_csv('ilike.csv', encoding='cp949')
places = pd.read_csv('places.csv', encoding='cp949')

str_num = input("몇 개의 여행지 추천을 하나요?? ")
num = int(str_num)

for i in range(0,1):
        types = input("당신의 여행 성향은 무엇인가요? ")
        for j in range(num):
            typess = types
            country = input("좋았던 나라는 어디인가요? ")
            city = input("어떤 도시를 여행했나요? ")

            liked = pd.concat([like, pd.DataFrame({'type': [typess], 'country': [country], 'city': [city]})], ignore_index=True)



same_type = pd.DataFrame(columns=['country', 'city'])
for i in range(len(places)):
   if places['type'][i] == liked['type'][0]:
       country = places['liked_country'][i]
       city = places['liked_city'][i]
       same_type = pd.concat([same_type, pd.DataFrame({'country': [country], 'city': [city]})], ignore_index=True)

print(same_type)
## 일단은 나라만 비교... 도시도 추천 나와야하나?!?!?!?!
missing_values = same_type[~same_type['country'].isin(liked['country'])]
print("missing_values")
print(missing_values)