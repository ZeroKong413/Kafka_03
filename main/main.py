from flask import Flask, request
import json
from time import sleep
from MP import MessageProducer

app = Flask(__name__)

broker = ["localhost:9094"]
topic = "my-topic"
pd = MessageProducer(broker, topic)

@app.route('/send_data', methods=['POST'])
def send_data():
    # POST 요청을 통해 받은 데이터 처리
    data = request.json
    # Kafka에 데이터 전송
    # 여기서 Kafka 프로듀서 코드를 작성
    # 브로커와 토픽명을 지정
    res = pd.send_message(data, False)

    return json.dumps(res)

if __name__ == '__main__':
    app.run(debug=True)
