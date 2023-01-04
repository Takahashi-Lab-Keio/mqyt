#!/usr/bin/env python
import paho.mqtt.client as mqtt     # MQTTのライブラリをインポート

class Subscriber:
    """
    a subscriber of mqtt topic message

    topic: topic name
    type: message type ("txt" or "img")
    func: callback function
    host: mqtt host
    port: port number
    """

    def __init__(self, topic, type, callback, host='broker.emqx.io', port=1883):
        self.func = callback
        self.type = type
        self.topic = topic

        # MQTTの接続設定
        self.client = mqtt.Client()                 # クラスのインスタンス(実体)の作成
        self.client.on_connect = self.on_connect         # 接続時のコールバック関数を登録
        self.client.on_disconnect = self.on_disconnect   # 切断時のコールバックを登録
        self.client.on_message = self.callback         # メッセージ到着時のコールバック

        self.client.connect(host, port, 60)  # 接続先はMQTTサーバー
        
        # 通信処理スタート
        self.client.loop_forever()                  # 永久ループして待ち続ける
        
    # ブローカーに接続できたときの処理
    def on_connect(self, client, userdata, flag, rc):
        print("Connected with result code " + str(rc))  # 接続できた旨表示
        client.subscribe(self.topic)  # subするトピックを設定 

    # ブローカーが切断したときの処理
    def on_disconnect(self, client, userdata, rc):
        if  rc != 0:
            print("Unexpected disconnection.")

    # メッセージが届いたときの処理
    def callback(self, client, userdata, msg):
        # msg.topicにトピック名が，msg.payloadに届いたデータ本体が入っている
        # print("Received message '" + str((msg.payload).decode('utf-8')) + "' on topic '" + msg.topic + "' with QoS " + str(msg.qos))
        if self.type == "txt":
            msg_str = str((msg.payload).decode('utf-8'))
            self.func(msg_str)

def callback(msg):
    print("callback result", msg)

if __name__ == "__main__":

    subscriber = Subscriber("topic_sub", "txt", callback)
