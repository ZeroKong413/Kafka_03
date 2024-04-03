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
    data = request.json

    res = pd.send_message(data, False)

    return json.dumps(res)

if __name__ == '__main__':
    app.run(debug=True)
