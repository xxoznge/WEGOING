import pandas as pd
# 좋았던 여행지 입력받기

like = pd.read_csv('ilike.csv', encoding='cp949')

def like_input(num):    
    ## 여행지 입력받는 개수를 정해놔야할까?
    for i in range(0,1):
        user = input("당신의 별명을 알려주세요 ")
        types = input("당신의 여행 성향은 무엇인가요? ")
        for j in range(num):
            user_id = user
            typess = types
            country = input("좋았던 나라는 어디인가요? ")
            city = input("어떤 도시를 여행했나요? ")

            liked = pd.concat([like, pd.DataFrame({'user_id': [user_id], 'type': [typess], 'country': [country], 'city': [city]})], ignore_index=True)

            return liked

like_input(2)