import random
import pandas as pd
import statistics
import matplotlib.pyplot as plt

from sklearn.metrics.pairwise import cosine_similarity
import operator

## 자기가 좋았던 여행지 입력
## 나랑 유사한 사용차 찾기
## 리스트 비교 후 없는 내용 출력

## @ 사용자가 입력한 여행지를 코드에서 받아와야하나? 아니면 csv로 받아오나???@##

like = pd.read_csv('ilike.csv', encoding='cp949')
places = pd.read_csv('places.csv', encoding='cp949')

