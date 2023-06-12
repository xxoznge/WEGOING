from flask import Flask, request, jsonify
import pandas as pd

app4 = Flask(__name__)
########################################save_option#####################################
selected_options = []

@app4.route('/save_option', methods=['POST'])
def save_option():
    data = request.json
    option = data[0].get('option')  # 첫 번째 요소의 'option' 키의 값을 가져옴
    question = data[0].get('question')  # 첫 번째 요소의 'question' 키의 값을 가져옴
    selected_options.append({'question': question, 'option': option})

    # selected_options 리스트를 pandas DataFrame으로 변환합니다
    df = pd.DataFrame(selected_options)

    # DataFrame을 CSV 파일로 저장합니다
    df.to_csv('selected_options.csv', index=False, header=True)
    return 'Option saved'


@app4.route('/get_options', methods=['GET'])
def get_options():
    return jsonify(selected_options)

if __name__ == '__main__':
    app4.run()
