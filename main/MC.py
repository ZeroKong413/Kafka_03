import requests
import json

url = 'http://127.0.0.1:5000/send_data'
data = {'age':'24', "name":"Kim"}  # 보낼 데이터를 딕셔너리로 정의

response = requests.post(url, json=data)
print(response.text)  # 서버로부터 받은 응답 출력
