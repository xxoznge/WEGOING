import pandas as pd

qna = pd.read_csv('qna.csv', encoding='cp949')
places = pd.read_csv('places.csv', encoding='cp949')
user = pd.read_csv('user.csv', encoding='cp949')
#user = pd.read_csv('user_input.csv', encoding='cp949')
an_input = pd.read_csv('selected_options.csv', encoding='cp949')

#abcd 리스트
a=[0]*(len(qna))
b=[0]*(len(qna))
c=[0]*(len(qna))
d=[0]*(len(qna))
def abcd():
    for i in range(0, len(qna),4):
        a[i]=qna['answer'][i]
        b[i]=qna['answer'][i+1]
        c[i]=qna['answer'][i+2]
        d[i]=qna['answer'][i+3]

    aa = [x for x in a if x != 0]
    bb = [x for x in b if x != 0]
    cc = [x for x in c if x != 0]
    dd = [x for x in d if x != 0]

    qna['answers'] = qna['answer']    #필요한가...?

    qna['answer'].replace(aa,'a',inplace=True)
    qna['answer'].replace(bb,'b',inplace=True)
    qna['answer'].replace(cc,'c',inplace=True)
    qna['answer'].replace(dd,'d',inplace=True)

    qna.to_csv('qqna.csv',encoding='cp949', index=False)

    return a, b, c, d

def cate_to_num(DataFrame):
    categories = ['모험가형', '문화 체험형', '휴양형', '음식 여행형', '자유 여행형', '문화 예술형']
    DataFrame['EncodedCategory'] = pd.factorize(DataFrame['type'])[0] + 1

def num_to_country(DataFrame):
    cate_to_num(DataFrame)
    DataFrame['c_to_n'] = pd.factorize(DataFrame['country'])[0]
    factorized_values = pd.factorize(DataFrame['c_to_n'])[0]
    #unique_categories = pd.factorize(DataFrame['c_to_n'])[1]
    unique_categories = DataFrame['country']
    # 숫자를 문자열로 변환
    converted_values = [unique_categories[index] for index in factorized_values]
    # 결과를 새로운 열로 추가
    DataFrame['n_to_c'] = converted_values

    # print(DataFrame['n_to_c'])
    return DataFrame

## 필요한 리스트 생성
an = pd.read_csv('result.csv',encoding='cp949')
result_in = ['0'] * len(an)

def an_to_abcd():
    for i in range(len(an)):
        q_num = i  # q_num 값을 i로 설정
        num = q_num * 4  ## 행 인덱스

        if an['option'][q_num] == qna['answers'][num]:
            result_in[q_num] = qna['answer'][num]
        elif an['option'][q_num] == qna['answers'][num + 1]:
            result_in[q_num] = qna['answer'][num + 1]
        elif an['option'][q_num] == qna['answers'][num + 2]:
            result_in[q_num] = qna['answer'][num + 2]
        elif an['option'][q_num] == qna['answers'][num + 3]:
            result_in[q_num] = qna['answer'][num + 3]

    result_in_df = pd.DataFrame({'result_in': result_in})
    result_in_df.to_csv('result_in.csv', encoding='cp949', index=False)
    return result_in