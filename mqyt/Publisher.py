#!/usr/bin/env python
import os
from dotenv import load_dotenv
import paho.mqtt.client as mqtt     # MQTTのライブラリをインポート
from time import sleep              # 3秒間のウェイトのために使う

class Publisher:

    def __init__(self):
        #環境変数の読み込み
        load_dotenv()
        # MQTTの接続設定
        self.client = mqtt.Client()                 # クラスのインスタンス(実体)の作成
        self.client.on_connect = self.on_connect         # 接続時のコールバック関数を登録
        self.client.on_disconnect = self.on_disconnect   # 切断時のコールバックを登録
        self.client.on_publish = self.on_publish         # メッセージ送信時のコールバック
        
        self.client.connect(os.environ["MQTT_HOST"], int(os.environ["MQTT_PORT"]), 60)  # 接続先はMQTTサーバー
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

    def publish(self, type, msg, topic=os.environ["MQTT_TOPIC_MESSAGE"]):
        """
        publish msg to remote server
        type: txt or image
        msg: publish data
        """
        if type == "txt":
            self.client.publish(topic, msg)    # トピック名とメッセージを決めて送信
            sleep(0.1)


if __name__ == "__main__":

    publisher = Publisher()
    publisher.publish("txt", "onishi")
