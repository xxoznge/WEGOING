from flask import Flask, request
import pandas as pd
################################테스트 결과 저장################################
app4 = Flask(__name__)

selected_options = []

@app4.route('/save_option', methods=['POST'])
def save_option():
    option = request.json['option']
    question = request.json['question']
    selected_options.append({'question': question, 'option': option})

    # selected_options 리스트를 pandas DataFrame으로 변환합니다
    df = pd.DataFrame(selected_options)

    # DataFrame을 CSV 파일로 저장합니다
    df.to_csv('selected_options.csv', index=False, header=True)
    return 'Option saved'


if __name__ == '__main__':
    app4.run()
