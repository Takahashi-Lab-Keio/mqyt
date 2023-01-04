#!/usr/bin/env python
import paho.mqtt.client as mqtt     # MQTTのライブラリをインポート
from time import sleep              # 3秒間のウェイトのために使う

class Publisher:
    """
    a publisher of mqtt topic message

    host: mqtt host
    port: port number
    """

    def __init__(self, host='broker.emqx.io', port=1883):
        # MQTTの接続設定
        self.client = mqtt.Client()                 # クラスのインスタンス(実体)の作成
        self.client.on_connect = self.on_connect         # 接続時のコールバック関数を登録
        self.client.on_disconnect = self.on_disconnect   # 切断時のコールバックを登録
        self.client.on_publish = self.on_publish         # メッセージ送信時のコールバック
        
        self.client.connect(host, port, 60)  # 接続先はMQTTサーバー
        sleep(0.2)

        # 通信処理スタート
        self.client.loop_start()    # subはloop_forever()だが，pubはloop_start()で起動だけさせる
        
    # ブローカーに接続できたときの処理
    def on_connect(self, client, userdata, flag, rc):
        print("Connected with result code " + str(rc))

    # ブローカーが切断したときの処理
    def on_disconnect(self, client, userdata, rc):
        if rc != 0:
            print("Unexpected disconnection.")

    # publishが完了したときの処理
    def on_publish(self, client, userdata, mid):
        print("publish: {0}".format(mid))

    def publish(self, topic, type, msg):
        """
        publish msg to remote server

        topic: topic name
        type: message type ("txt" or "img")
        msg: published msg
        """
        if type == "txt":
            self.client.publish(topic, msg)    # トピック名とメッセージを決めて送信
            sleep(0.1)


if __name__ == "__main__":

    publisher = Publisher()
    publisher.publish("topic_pub", "txt", "ytlab")
