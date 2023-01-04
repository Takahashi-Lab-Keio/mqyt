# mqyt

mqyt is a Python Library for communication among local scripts and remote server via MQTT.

## Installation

```shell
pip install git+git@github.com:Takahashi-Lab-Keio/mqyt.git
```


## Tutorial
### Publisher

```python
from mqyt import Publisher

# create publisher instance
publisher = Publisher()

# publish message
# type: "txt" or "img", msg: published data, topic: topic name
publisher.publish(type="txt", msg="ytlab", topic="robot-action-pub/001")
```
### Subscriber

```python
from mqyt import Subscriber

# callback function that called when the topic is subscribed
def callback(msg):
    print("calback_result", msg)

if __name__ == "__main__":
    # create subscriber instance
    # type: "txt" or "img", callback: callback function, topic: topic name
    subscriber = Subscriber(type="txt", callback=callback, topic="robot-action/001")

```

## Sample application
https://github.com/Takahashi-Lab-Keio/ytlab_IoT_robotics

## License
Copyright &copy; 2022 Takahashi Lab.
Licensed under the MIT license.